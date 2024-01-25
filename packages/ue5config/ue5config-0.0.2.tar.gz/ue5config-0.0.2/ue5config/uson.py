"""
I don't know what the Hell to call this, but it's sort of a JSON-like object notation that I've 
seen PalWorld use, so I suspect it's a UE thing as well.  Epic probably has some fancy name for it,
but I'm just calling it Unreal Scripted Object Notation, or USON.

This is a garbage implementation, I know. Deal with it.
"""
import json
from typing import Any


class InvalidTypeException(Exception):
    pass


def is_float(s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False


class USONSerializer:
    def __init__(self) -> None:
        pass

    def serialize(self, v: Any) -> str:
        if isinstance(v, dict):
            return self.serialize_dict(v)
        if isinstance(v, list):
            return self.serialize_list(v)
        if isinstance(v, int):
            return self.serialize_int(v)
        if isinstance(v, float):
            return self.serialize_float(v)
        if isinstance(v, str):
            return self.serialize_str(v)
        if isinstance(v, bool):
            return self.serialize_bool(v)
        if v is None:
            return "None"
        raise InvalidTypeException(type(v))

    def serialize_str(self, v: str) -> str:
        if (
            v == ""
            or v in ("True", "False", "None")
            or is_float(v)
            or v.isdecimal()
            or " " in v
            or '"' in v
            or "," in v
            or "(" in v
            or ")" in v
            or "{" in v
            or "}" in v
            or "//" in v
            or "\\" in v
            or "\n" in v
            or "\r" in v
            or "=" in v
        ):
            return json.dumps(v)
        return v

    def serialize_float(self, v: float) -> str:
        # why
        return f"{v:0.6f}"

    def serialize_int(self, v: int) -> str:
        return str(v)

    def serialize_bool(self, v: bool) -> str:
        return str(v)

    def serialize_dict(self, d: dict) -> str:
        return (
            "(" + (",".join([k + "=" + self.serialize(v) for k, v in d.items()])) + ")"
        )

    def serialize_list(self, l: list) -> str:
        return "[" + (",".join([self.serialize(i) for i in l])) + "]"
