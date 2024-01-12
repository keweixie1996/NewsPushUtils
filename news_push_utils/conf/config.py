# -*- coding:utf-8 -*-

from pathlib import Path
import configparser
import yaml


HOME_DIR = Path(__file__).parents[1].resolve()
CONF_DIR = Path(HOME_DIR, "conf")


DEV = True


config = yaml.safe_load(open(Path(CONF_DIR, "config.yaml")))

blockbeats_wss = config["blockbeats"]["wss"]

discord_wehook_base = config["discord"]["webhook"]

