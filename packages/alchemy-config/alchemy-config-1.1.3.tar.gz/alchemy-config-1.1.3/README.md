# Alchemy Config
The `aconfig` library provides simple `yaml` configuration in `python` with environment-based overrides.

## Installation

To install, simply use `pip`

```sh
pip install alchemy-config
```

## Quick Start

**config.yaml**
```yaml
foo: 1
bar:
    baz: "bat"
```

**main.py**
```py
import aconfig

if __name__ == "__main__":
    config = aconfig.Config.from_yaml("config.yaml")
    print(config.foo)
    print(config.bar.baz)
```

```sh
export BAR_BAZ="buz"
python3 main.py
```

## Corner-case Behavior

You CAN set builtin method names as attributes on the `config`. However, you should only access/delete them via dictionary access methods.

For example:

```py
import aconfig
cfg = {"update": True}

config = aconfig.Config(cfg)

# DO NOT DO THIS:
config.update

# DO THIS INSTEAD:
config["update"]
```

This is because there is no way in Python to tell whether you want the method or the attribute `"update"` when "getting" it from the object.
