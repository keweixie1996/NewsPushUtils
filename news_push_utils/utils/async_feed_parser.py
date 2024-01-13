# -*- coding: utf-8 -*-


import aiohttp
import asyncio
import logging
import itertools
import json
import sys
import requests
import time
import feedparser
from bs4 import BeautifulSoup
from asyncio import to_thread
from aiohttp import BasicAuth
from typing import Union, Optional

#from news_push_utils.utils.retry import retry




class AsyncFeedParser(object):

    def __init__(self):
        pass

    async def feed_parser(self, endpoint: str) -> dict:
        try:
            response = await to_thread(feedparser.parse, endpoint)
            return {"success": True, "response": response}
        except Exception as e:
            return {"success": False, "error": str(e)}



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
    print(json.dumps(news["response"]["entries"][1], indent=1))
    #res = BeautifulSoup(news["response"]["entries"][1]["summary"], "html.parser")
    #print(res.find_all("p")[0].text)



if __name__ == "__main__":
    asyncio.run(main())
