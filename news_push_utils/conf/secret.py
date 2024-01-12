# -*- coding: utf-8 -*-



from pathlib import Path
import yaml

try:
    from .config import CONF_DIR, DEV
except:
    from config import CONF_DIR, DEV


secret = yaml.safe_load(open(Path(CONF_DIR, "secret.yaml")))


discord_secret = secret["discord"]
discord_webhook = discord_secret["blockbeats" if not DEV else "dev"]
discord_webhook_auth = (
    f"{discord_webhook['channel']}"
    f"/{discord_webhook['token']}"
)
