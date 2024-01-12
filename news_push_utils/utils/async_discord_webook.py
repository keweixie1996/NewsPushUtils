# -*- coding: utf-8 -*-


import aiohttp
import asyncio
import logging
import itertools
import json
import sys
import time
from bs4 import BeautifulSoup
from asyncio import to_thread
from typing import Union, Optional
from discord_webhook import DiscordWebhook, DiscordEmbed

#from news_push_utils.utils.retry import retry




class AsyncDiscordWebook(object):

    def __init__(self, auth):
        self.endpoint = f"https://discord.com/api/webhooks/{auth}"


    async def webhook_sender(self, content, embed):
        webhook = DiscordWebhook(url=self.endpoint, content=content)
        webhook.add_embed(embed)
        response = webhook.execute()
        print(response)


    def build_embed(self, title, url, description, author_name):
        embed = DiscordEmbed(
            title = title,
            url = url,
            description = description,
        )
        embed.set_author(name=author_name)
        return embed


async def main():

    wss_url = "https://api.theblockbeats.news/v1/open-api/home-xml"
    #client = AsyncFeedParser()
    #result = await client.feed_parser(wss_url)
    #print(json.dumps(result, indent=1))
    #with open("demo-news", "w") as fw:
    #    fw.write(f"{json.dumps(result)}")
    news = json.loads(open("demo-news").read())
    print(news["response"]["entries"][0].keys())
    print(news["response"]["entries"][0]["title"])
    #print(news["response"]["entries"][0]["title_detail"]["value"])
    print(news["response"]["entries"][0]["link"])
    #print(news["response"]["entries"][0]["summary"])
    print(news["response"]["entries"][1]["summary"].split("<br />")[0])
    #print(json.dumps(news["response"]["entries"][1], indent=1))
    res = BeautifulSoup(news["response"]["entries"][1]["summary"])
    print(res.find_all("p")[0].text)

    url = news["response"]["entries"][1]["link"]
    author = "律动 BlockBeats"
    title = news["response"]["entries"][1]["title"]
    description = res.find_all("p")[0].text
    auth = ""
    discord_webhook = AsyncDiscordWebook(auth=auth)
    discord_embed = discord_webhook.build_embed(
        title = title,
        url = url,
        description = description,
        author_name = author,
    )
    await discord_webhook.webhook_sender(title, discord_embed)



if __name__ == "__main__":
    asyncio.run(main())

