import csv
import json
import logging
import math
import parser
import unittest

from ebooklib import epub
from fpdf import FPDF
from bs4 import BeautifulSoup
import csv
import requests
import json
import logging
from fpdf import FPDF
from ebooklib import epub
import publishing_date
import rss_reader
from rss_packaging import rss_read, argparse_rss
from rss_packaging.argparse_rss import *
from rss_packaging.rss_read import *
from unittest import TestCase, main


class RSS_reader_tests(TestCase):

    def test_reader_rss(self):
        self.main_link = "https://www.nasa.gov/rss/dyn/breaking_news.rss"
        self.limit = 1
        self.assertIsNone(rss_read.reader_rss(self))

    def test_reader_rss_with_json_format(self):
        self.main_link = "https://lenta.ru/rss"
        self.limit = 2
        self.assertIsNot(rss_read.reader_rss_with_json_format(self),"'NoneType' object has no attribute 'text'\n "
                                                                    "This news didn't write in local_storage ")

    def test_content_local_storage(self):
        self.main_link = "https://www.nasa.gov/rss/dyn/breaking_news.rss"
        self.limit = 1
        self.assertIsNone(rss_read.content_local_storage(self))

    def test_reader_rss_with_loggs(self):
        self.main_link = "https://www.nasa.gov/rss/dyn/breaking_news.rss"
        self.limit = 2
        self.assertIsNot(rss_read.reader_rss_with_loggs(self), "'NoneType' object has no attribute 'text'")

    def test_convert_news_in_pdf(self):
        self.main_link = "https://lenta.ru/rss"
        self.limit = 2
        self.assertIsNone(rss_read.convert_news_in_pdf(self))

    def test_convert_news_in_epub(self):
        self.main_link = "https://www.nasa.gov/rss/dyn/breaking_news.rss"
        self.limit = 1
        self.assertIsNone(rss_read.convert_news_in_epub(self))


if __name__ == "__main__":
    unittest.main()