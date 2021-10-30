import math

from bs4 import BeautifulSoup
import csv
import requests
import json
import logging
from fpdf import FPDF
from ebooklib import epub


class Rss_reader:

    def __init__(self, main_link, limit):
        self.main_link = main_link
        self.items = str()
        self.limit = limit

    def reader_rss(self):
        # default parser without additional options
        url = requests.get(self.main_link)
        soup = BeautifulSoup(url.content, "xml")
        self.items = soup.find_all("item")
        channel = soup.find_all("channel")
        feed = channel[0].title.text
        print(f"\nFeed: {feed}\n")

        for item in self.items[:self.limit]:
            try:
                title = item.title.text
                pubDate = item.pubDate.text
                link = item.link.text
                description = item.description.text
            except AttributeError:
                raise "'NoneType' object has no attribute 'text'"
            print(f"Title: {title}\nDate: {pubDate} \nLink: {link}\n\n{description}\n\n")

    def reader_rss_with_json_format(self):
        # parser that return news with json format
        json_dict = {}
        json_dict["feed"], json_dict["structure_of_our_json"] = {}, {}

        url = requests.get(self.main_link)
        soup = BeautifulSoup(url.content, "xml")
        self.items = soup.find_all("item")
        channel = soup.find_all("channel")
        json_dict["feed"] = channel[0].title.text

        for item in self.items[:self.limit]:
            try:
                json_dict["structure_of_our_json"]["title"] = item.title.text
                json_dict["structure_of_our_json"]["pubDate"] = item.pubDate.text
                json_dict["structure_of_our_json"]["link"] = item.link.text
                json_dict["structure_of_our_json"]["description"] = item.description.text
            except AttributeError:
                raise "'NoneType' object has no attribute 'text'"
            new_json = json.dumps(json_dict, indent=3, ensure_ascii=False)
            print(new_json)

    def reader_rss_with_loggs(self):
        # return loggs of this parser
        logging.basicConfig(level=logging.DEBUG,
                            format="%(levelname)s %(asctime)s - %(message)s")
        logger = logging.getLogger()

        logger.info("getting url")
        url = requests.get(self.main_link)
        soup = BeautifulSoup(url.content, "xml")
        self.items = soup.find_all("item")
        logger.debug("get the feed site")

        for count, item in enumerate(self.items[:self.limit], start=1):
            logger.debug(f"parsing the {count} news")
            try:
                logger.debug(f"getting the title of the {count} site")
                title = item.title.text
                logger.debug(f"getting the pubDate of the {count} site")
                pubDate = item.pubDate.text
                logger.debug(f"getting the link of the {count} site")
                link = item.link.text
                logger.debug(f"getting the description of the {count} site\n")
                description = item.description.text
            except AttributeError:
                logger.error("'NoneType' object has no attribute 'text'")
