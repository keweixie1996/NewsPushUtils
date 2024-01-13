# -*- coding:utf-8 -*-

from pathlib import Path
import configparser
import yaml


HOME_DIR = Path(__file__).parents[1].resolve()
CONF_DIR = Path(HOME_DIR, "conf")


DEV = True
CACHE = "file"      # file or db


config = yaml.safe_load(open(Path(CONF_DIR, "config.yaml")))

discord_wehook_base = config["discord"]["webhook"]


blockbeats_wss = config["blockbeats"]["wss"]
blockbeats_cache_path = Path(config["cache"][CACHE]).expanduser()
blockbeats_cache_path.mkdir(parents=True, exist_ok=True)

