# -*- coding:utf-8 -*-

import asyncio
import logging

from operator import itemgetter
from pathlib import Path
from bs4 import BeautifulSoup

import news_push_utils.conf.config as conf
import news_push_utils.utils.datetime_util as dt_tools
from news_push_utils.utils import AsyncFeedParser
from news_push_utils.utils import AsyncDiscordWebhook


def pushlied_convert(pushlied):
    dt = dt_tools.client2datetime(pushlied, False)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def load_push_history():
    history_path = conf.blockbeats_cache_path
    push_history = set({})
    for file in history_path.iterdir():
        push_history |= set(open(file).read().strip().split("\n"))
    return push_history


async def news_parser(news_response, history):
    def core(news):
        soup = BeautifulSoup(news["summary"], "lxml")
        description = soup.find_all("p")[0].text
        ptime = pushlied_convert(news["published"])
        return (news["id"], {
            "id": news["id"],
            "author_name": "律动 BlockBeats",
            "title": f"[{ptime}] {news['title']}",
            "url": news["link"],
            "description": description,
            "published": ptime,
        })
    if not news_response["success"]:
        return []
    candidate_news = []
    for news in news_response["response"]["entries"]:
        if news["id"] in history: continue
        news_id, news_info = core(news)
        candidate_news.append(news_info)

    candidate_news = sorted(
        candidate_news,
        key=itemgetter("published"),
    )
    return candidate_news


async def push(discord_webhook_auth):

    cache_file = Path(
        conf.blockbeats_cache_path,
        dt_tools.get_current_date(),
    )
    push_history = load_push_history()

    feed_parser = AsyncFeedParser()
    discord_webhook = AsyncDiscordWebhook(auth=discord_webhook_auth)

    news_response = await feed_parser.feed_parser(
        endpoint=conf.blockbeats_wss,
    )
    candidate_news = await news_parser(news_response, push_history)

    for news in candidate_news:
        logging.info(f"NewsPush[{news['url']}][{news['title']}]")
        embed = discord_webhook.build_embed(
            title = news["title"],
            url = news["url"],
            description = news["description"],
            author_name = news["author_name"],
        )
        await discord_webhook.webhook_sender(news["title"], embed)

        with open(cache_file, "a+") as fw:
            fw.write(f"{news['id']}\n")
        push_history.add(news["id"])

        await asyncio.sleep(5)


