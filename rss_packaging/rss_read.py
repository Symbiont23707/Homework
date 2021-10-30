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

    def content_local_storage(self):
        # save news in local storage for "--date"
        with open("temporary_storage.csv", mode="a", encoding="utf-8") as w_file:
            csv.register_dialect('temporary_storage', lineterminator="\r")
            file_writer = csv.writer(w_file, 'temporary_storage')
            url = requests.get(self.main_link)
            soup = BeautifulSoup(url.content, "xml")
            self.items = soup.find_all("item")
            channel = soup.find_all("channel")
            feed = channel[0].title.text

            for item in self.items[:self.limit]:
                try:
                    title = item.title.text
                    pubDate = item.pubDate.text
                    link = item.link.text
                    description = item.description.text
                except AttributeError:
                    raise "'NoneType' object has no attribute 'text'\n This news didn't write in local_storage "

                file_writer.writerow([feed, title, pubDate, link, description])

    def convert_news_in_pdf(self):
        #function that convert news in pdf

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        url = requests.get(self.main_link)
        soup = BeautifulSoup(url.content, "xml")
        self.items = soup.find_all("item")
        channel = soup.find_all("channel")
        feed = channel[0].title.text

        for item in self.items[:self.limit]:
            try:
                title = item.title.text
                pubDate = item.pubDate.text
                link = item.link.text
                description = str(item.description.text.encode("ascii", "ignore"))
            except AttributeError:
                raise "'NoneType' object has no attribute 'text'\n This news didn't write in local_storage "
            n = 2
            pdf.cell(0, 10, txt=f"Feed: {feed}", ln=1)
            pdf.cell(0, 5, txt=f"Title: {title}", ln=1)
            pdf.cell(0, 5, txt=f"PubDate: {pubDate}", ln=1)
            pdf.cell(0, 5, txt=f"Link: {link}", ln=1)
            pdf.cell(0, 5, txt=f"Description: {description[n:70]}", ln=1)
            n += 69

            for new_line in range(math.ceil(len(description) / 69)):
                pdf.cell(0, 5, txt=f"{description[n:69 + n]}", ln=1)
                n += 69
        pdf.output("newsPDF.pdf")

    def convert_news_in_epub(self):
        # function that convert news in epub
        temporarily_content = ""
        book = epub.EpubBook()
        book.set_identifier('id1')
        book.set_title('NewsEPUB')
        book.add_author('Evgeny Bykov')

        url = requests.get(self.main_link)
        soup = BeautifulSoup(url.content, "xml")
        self.items = soup.find_all("item")
        channel = soup.find_all("channel")
        feed = channel[0].title.text

        c1 = epub.EpubHtml(title='newsEPUB', file_name='chap.xhtml')
        for item in self.items[:self.limit]:
            try:
                title = item.title.text
                pubDate = item.pubDate.text
                link = item.link.text
                description = str(item.description.text.encode("ascii", "ignore"))
            except AttributeError:
                raise "'NoneType' object has no attribute 'text'\n This news didn't write in local_storage "
            c1_content = f"<p>{feed}</p><p>Title: {title} </p>" \
                         f"<p>Date: {pubDate}</p>" \
                         f"<p>Link: {link}</p>" \
                         f"<p>{description[2:-1]}</p>"
            temporarily_content += c1_content
        c1.content = temporarily_content
        book.add_item(c1)

        book.toc = epub.Section('newsEPUB'), c1

        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        epub.write_epub('newsEPUB.epub', book, {})
#########################################################
#unittest
#########################################################
##for unittest(without this functions i have errors)
def reader_rss(self):
    # default parser without additional options(for unittests)
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


def content_local_storage(self):
    # save news in local storage for "--date"
    with open("temporary_storage.csv", mode="a", encoding="utf-8") as w_file:
        csv.register_dialect('temporary_storage', lineterminator="\r")
        file_writer = csv.writer(w_file, 'temporary_storage')
        url = requests.get(self.main_link)
        soup = BeautifulSoup(url.content, "xml")
        self.items = soup.find_all("item")
        channel = soup.find_all("channel")
        feed = channel[0].title.text

        for item in self.items[:self.limit]:
            try:
                title = item.title.text
                pubDate = item.pubDate.text
                link = item.link.text
                description = item.description.text
            except AttributeError:
                raise "'NoneType' object has no attribute 'text'\n This news didn't write in local_storage "

            file_writer.writerow([feed, title, pubDate, link, description])


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


def convert_news_in_pdf(self):
    # function that convert news in pdf

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    url = requests.get(self.main_link)
    soup = BeautifulSoup(url.content, "xml")
    self.items = soup.find_all("item")
    channel = soup.find_all("channel")
    feed = channel[0].title.text

    for item in self.items[:self.limit]:
        try:
            title = item.title.text
            pubDate = item.pubDate.text
            link = item.link.text
            description = str(item.description.text.encode("ascii", "ignore"))
        except AttributeError:
            raise "'NoneType' object has no attribute 'text'\n This news didn't write in local_storage "
        n = 2
        pdf.cell(0, 10, txt=f"Feed: {feed}", ln=1)
        pdf.cell(0, 5, txt=f"Title: {title}", ln=1)
        pdf.cell(0, 5, txt=f"PubDate: {pubDate}", ln=1)
        pdf.cell(0, 5, txt=f"Link: {link}", ln=1)
        pdf.cell(0, 5, txt=f"Description: {description[n:70]}", ln=1)
        n += 69

        for new_line in range(math.ceil(len(description) / 69)):
            pdf.cell(0, 5, txt=f"{description[n:69 + n]}", ln=1)
            n += 69
    pdf.output("newsPDF.pdf")


def convert_news_in_epub(self):
    # function that convert news in epub
    temporarily_content = ""
    book = epub.EpubBook()
    book.set_identifier('id1')
    book.set_title('NewsEPUB')
    book.add_author('Evgeny Bykov')

    url = requests.get(self.main_link)
    soup = BeautifulSoup(url.content, "xml")
    self.items = soup.find_all("item")
    channel = soup.find_all("channel")
    feed = channel[0].title.text

    c1 = epub.EpubHtml(title='newsEPUB', file_name='chap.xhtml')
    for item in self.items[:self.limit]:
        try:
            title = item.title.text
            pubDate = item.pubDate.text
            link = item.link.text
            description = str(item.description.text.encode("ascii", "ignore"))
        except AttributeError:
            raise "'NoneType' object has no attribute 'text'\n This news didn't write in local_storage "
        c1_content = f"<p>{feed}</p><p>Title: {title} </p>" \
                     f"<p>Date: {pubDate}</p>" \
                     f"<p>Link: {link}</p>" \
                     f"<p>{description[2:-1]}</p>"
        temporarily_content += c1_content
    c1.content = temporarily_content
    book.add_item(c1)

    book.toc = epub.Section('newsEPUB'), c1

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub.write_epub('newsEPUB.epub', book, {})