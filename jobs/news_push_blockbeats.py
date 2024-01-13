# -*- coding:utf-8 -*-

import asyncio
import logging
import sys

sys.path.append("..")

from news_push_utils import blockbeats_discord
from news_push_utils.conf.secret import discord_webhook_auth
from news_push_utils.utils.common_util import init_logging




async def main():

    init_logging()

    auth = discord_webhook_auth
    await blockbeats_discord.push(auth)



if __name__ == "__main__":
    asyncio.run(main())
