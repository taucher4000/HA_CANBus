#!/canbus/bin/python3
# -*- coding: utf-8 -*-
import json
import yaml
import sys
from pathlib import Path
from miqro_can.canbus import CANService
import miqro
import random
from time import sleep


CONFIG_FILE = Path("/etc/miqro.yml")
OPTIONS_FILE = Path("/data/options.json")

MIQRO_CONFIG = {
    "broker": {
        "host": "core-mosquitto",
        "port": 1883,
        "keepalive": 60
    },
    "auth": {
        "username": "",
        "password": ""
    },
    "log_level": "INFO",
    "services": {
        "can": {}
    }
}

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data: dict, path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

ha_options = load_json(OPTIONS_FILE)

MIQRO_CONFIG["broker"]["host"] = ha_options["MQTTBroker"]
MIQRO_CONFIG["auth"]["username"] = ha_options["MQTTUser"]
MIQRO_CONFIG["auth"]["password"] = ha_options["MQTTPassword"]
MIQRO_CONFIG["log_level"] = "DEBUG" if ha_options["Debug"] else "INFO"

save_yaml(MIQRO_CONFIG, CONFIG_FILE)

if __name__ == '__main__':
    while True:
        print("This loop will run forever!")
        sleep(10)

#    sys.exit(miqro.run(CANService))
