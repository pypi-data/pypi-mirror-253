# UE5Config

_A config file parsing solution for Unreal 5._

A grammatical parsing library for [Unreal Engine 5 configuration files](https://docs.unrealengine.com/5.2/en-US/configuration-files-in-unreal-engine/), born out of a need to be able to make sense of PalWorld dedicated server configuration files.

## NOTICES

This code tries to parse UE5 configuration data correctly, but due to its immaturity, it may get it wrong.  You are responsible for checking output prior to usage. You risk losing data if you've not made backups.  Please file a bug report if something is incorrect.

While I have a UE license, I have not based this library off of any Unreal Engine code.  The syntax was made by eyeballing PalWorld and Satisfactory configuration files and slapping around pyparsing until it worked.

This code is by no means the most efficient way of doing things, either.

## Installation

Please note that this software is designed to be used by your own scripts or application and doesn't have its own front end.

Release builds of this software is available on pypi as [`ue5config`](https://pypi.org/project/ue5config/).

### poetry

To install UE5Config in your [poetry](https://python-poetry.org/) project:

```shell
poetry add ue5config
```

To install the most cutting-edge (and possibly broken) code, use our gitlab repo:

```shell
poetry add git+https://gitlab.com/N3X15/UE5Config.git
```

### pipx

To install UE5Config into your [pipx](https://github.com/pypa/pipx) project:

```shell
pipx install ue5config
```

To install the most cutting-edge (and possibly broken) code, use our gitlab repo:

```shell
pipx install git+https://gitlab.com/N3X15/UE5Config.git@dev
```

### pip

To install UE5Config **globally**:

```shell
sudo pip install ue5config
```

To install the most cutting-edge (and possibly broken) code, use our gitlab repo:

```shell
sudo pip install git+https://gitlab.com/N3X15/UE5Config.git
```


## How to use

```python
from pathlib import Path

from ue5config import UE5Config

cfg = UE5Config()
cfg.read_file((Path("samples") / "DefaultPalWorldSettings.ini"))

# Dump to JSON
cfg.write_json(Path("samples") / "DefaultPalWorldSettings.json", indent=2)

# Dump to YAML - requires ruamel.yaml package
cfg.write_yaml(Path("samples") / "DefaultPalWorldSettings.yml")

# Dump to TOML - requires toml package
cfg.write_toml(Path("samples") / "DefaultPalWorldSettings.toml")

## Mess around

# Get the main section
palworld_section = cfg.get_or_create("/Script/Pal.PalGameWorldSettings")

# Get the option all the settings are crammed into for some reason
optsettings = palworld_section["OptionSettings"]
# Change stuff
optsettings["ServerName"] = "Grugworld"
optsettings["ServerPlayerMaxNum"] = 64
optsettings["PlayerStomachDecreaceRate"] = 0.01
optsettings["ServerDescription"] = "Brought to you by the Eggman Empire"
# NOTE: If the value is something like All (no quotes), it's just an unquoted string.
optsettings["DeathPenalty"] = "All"

## Saving
cfg.write_file(Path("samples") / "MyServerSettings.ini")
```

## License

This library is available to you under the terms of the MIT Open Source License. See [LICENSE](LICENSE) for more details.

