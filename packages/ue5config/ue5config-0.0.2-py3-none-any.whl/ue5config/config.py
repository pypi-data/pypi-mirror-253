import collections
from pathlib import Path
from typing import Any, Callable, Iterator, MutableMapping, Optional, OrderedDict

import pyparsing as pyp

from ue5config.syntax import SYNTAX
from ue5config.uson import USONSerializer

__all__ = ["UE5Config"]


class UE5Config(MutableMapping[str, Any]):
    def __init__(self) -> None:
        super().__init__()
        self.filename: Optional[Path] = None
        self.values: OrderedDict[str, OrderedDict[str, Any]] = collections.OrderedDict()

    def read_string(self, instr: str) -> None:
        self.filename = None
        try:
            res = SYNTAX.parse_string(instr)
            self._load_as_list(res.as_list())
        except pyp.ParseException as e:
            self.handle_parse_exception(e)
            return

    def read_file(self, path: Path) -> None:
        self.filename = path
        try:
            res = SYNTAX.parse_file(path)
            self._load_as_list(res.as_list())
        except pyp.ParseException as e:
            self.handle_parse_exception(e)
            return

    def handle_parse_exception(self, err: pyp.ParseException) -> None:
        print(
            "[!] {FILENAME}:{LINE}:{COLUMN}:".format(
                FILENAME=(
                    "<string>"
                    if self.filename is None
                    else str(self.filename.absolute())
                ),
                LINE=err.lineno,
                COLUMN=err.column,
            )
        )
        print("  " + err.line)
        print("  " + ("-" * (err.column - 1)) + "^")
        print(err)

    def _load_as_list(self, l: list) -> None:
        self.values.clear()
        for section in l:
            section_header = section[0]
            section_body = section[1:]
            section_data = collections.OrderedDict()
            for k, v in section_body:
                i: Optional[str] = None
                # why.
                if k[0] in ("!", "-", "+", "."):
                    i = k[0]
                    k = k[1:]
                match i:
                    case None:
                        if k not in section_data:
                            section_data[k] = v
                        else:
                            if isinstance(section_data[k], list):
                                section_data[k].append(v)
                            else:
                                section_data[k] = [section_data[k], v]
                    case "!":  # Clear
                        section_data[k] = []
                    case "+":  # Add
                        if k not in section_data:
                            section_data[k] = [v]
                        else:
                            if isinstance(section_data[k], list):
                                if v not in section_data[k]:
                                    section_data[k].append(v)
                            else:
                                section_data[k] = [v]
                    case "-":
                        if k in section_data:
                            if isinstance(section_data[k], list):
                                section_data[k].remove(v)
                    case ".":  # Append/Duplicate
                        if k not in section_data:
                            section_data[k] = [v]
                        else:
                            if isinstance(self.values[k], list):
                                section_data[k].append(v)
                            else:
                                section_data[k] = [v]
            self.values[section_header] = section_data

    def write_file(self, path: Path) -> None:
        ser = USONSerializer()
        with path.open("w") as f:
            for section_header, section in self.values.items():
                f.write(f"[{section_header}]\n")
                for k, v in section.items():
                    if isinstance(v, list):
                        for e in v:
                            f.write(f"{k}={ser.serialize(e)}\n")
                    else:
                        f.write(f"{k}={ser.serialize(v)}\n")

    def write_json(
        self,
        path: Path,
        *,
        skipkeys: bool = False,
        ensure_ascii: bool = True,
        check_circular: bool = True,
        allow_nan: bool = True,
        sort_keys: bool = False,
        indent: int | str | None = None,
        separators: tuple[str, str] | None = None,
        default: Callable[..., Any] | None = None,
    ) -> None:
        import json

        with path.open("w") as f:
            json.dump(
                self.values,
                f,
                skipkeys=skipkeys,
                ensure_ascii=ensure_ascii,
                check_circular=check_circular,
                allow_nan=allow_nan,
                indent=indent,
                separators=separators,
                default=default,
                sort_keys=sort_keys,
            )

    def write_yaml(
        self,
        path: Path,
        typ: Optional[str] = None,
        pure: bool = False,
        default_flow_style: Any = False,
    ) -> None:
        from ruamel.yaml import YAML as Yaml
        from ruamel.yaml.representer import SafeRepresenter

        YAML = Yaml(typ=typ, pure=pure)
        # Fix flow style
        YAML.default_flow_style = default_flow_style
        # Remove !!omap
        r: SafeRepresenter = YAML.representer
        r.add_representer(collections.OrderedDict, YAML.Representer.represent_dict)
        # YAML.indent()
        with path.open("w") as f:
            YAML.dump(self.values, f)

    def write_toml(
        self,
        path: Path,
    ) -> None:
        import toml

        t = toml.TomlEncoder()
        with path.open("w") as f:
            toml.dump(self.values, f, encoder=t)

    def __getitem__(self, __key: str) -> Any:
        return self.values.__getitem__(__key)

    def __setitem__(self, __key: str, __value: Any) -> None:
        return self.values.__setitem__(__key, __value)

    def __delitem__(self, __key: str) -> None:
        return self.values.__delitem__(__key)

    def __iter__(self) -> Iterator[str]:
        return self.values.__iter__()

    def __len__(self) -> int:
        return self.values.__len__()

    def get_or_create(
        self,
        section: str,
        initial_values: Optional[OrderedDict[str, Any]] = None,
    ) -> OrderedDict[str, Any]:
        if section not in self.values:
            self.values[section] = initial_values or collections.OrderedDict()
        return self.values[section]

    def get_section(self, section: str) -> Optional[OrderedDict[str, Any]]:
        return self.values.get(section)

    def set_section(self, section: str, data: OrderedDict[str, Any]) -> None:
        self.values[section] = data

    def del_section(self, section: str) -> None:
        del self.values[section]

    def get_key(self, section: str, key: str, default: Any = None) -> Any:
        if section not in self.values or key not in self.values[section]:
            return default
        return self.values[section][key]

    def get_or_create_key(
        self, section: str, key: str, initial_value: Any = None
    ) -> Any:
        sec = self.get_or_create(section)
        if key not in sec:
            sec[key] = initial_value
        return self.values[section][key]

    def set_key(self, section: str, key: str, value: Any) -> None:
        self.get_or_create(section)[key] = value
