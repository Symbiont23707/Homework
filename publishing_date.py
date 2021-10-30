import csv
import json
import logging
import math

from ebooklib import epub
from fpdf import FPDF

months = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Deс": "12"
}

def get_date(str_date, limit=0):
    #loading the news on the screen by a certain date

    with open("temporary_storage.csv", encoding="utf-8") as r_file:
        count = 0
        if limit == None:
            limit = 0
        file_reader = csv.reader(r_file)
        if count < limit:
            for row in file_reader:
                if count < limit:
                    if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and\
                            months[row[2][8:11]] == str_date[4:6]:
                        print(f"Feed: {row[0]}\n\nTitle: {row[1]}\nDate: {row[2]} \nLink: {row[3]}\n\n{row[4]}\n\n")
                        count += 1
        else:
            for row in file_reader:
                if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and\
                        months[row[2][8:11]] == str_date[4:6]:
                    print(f"Feed: {row[0]}\n\nTitle: {row[1]}\nDate: {row[2]} \nLink: {row[3]}\n\n{row[4]}\n\n")

def get_date_json(str_date, limit=0):
    # loading the news on the screen by a certain date in json format

    with open("temporary_storage.csv", encoding="utf-8") as r_file:
        count = 0
        if limit == None:
            limit = 0
        json_dict = {}
        json_dict["feed"], json_dict["structure_of_our_json"] = {}, {}
        file_reader = csv.reader(r_file)
        if count < limit:
            for row in file_reader:
                if count < limit:
                    if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and \
                            months[row[2][8:11]] == str_date[4:6]:
                        try:
                            json_dict["feed"] = row[0]
                            json_dict["structure_of_our_json"]["title"] = row[1]
                            json_dict["structure_of_our_json"]["pubDate"] = row[2]
                            json_dict["structure_of_our_json"]["link"] = row[3]
                            json_dict["structure_of_our_json"]["description"] = row[4]
                        except AttributeError:
                            raise "'NoneType' object has no attribute 'text'"
                        new_json = json.dumps(json_dict, indent=3, ensure_ascii=False)
                        print(new_json)
                        count += 1
        else:
            for row in file_reader:
                if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and \
                        months[row[2][8:11]] == str_date[4:6]:
                    try:
                        json_dict["feed"] = row[0]
                        json_dict["structure_of_our_json"]["title"] = row[1]
                        json_dict["structure_of_our_json"]["pubDate"] = row[2]
                        json_dict["structure_of_our_json"]["link"] = row[3]
                        json_dict["structure_of_our_json"]["description"] = row[4]
                    except AttributeError:
                        raise "'NoneType' object has no attribute 'text'"
                    new_json = json.dumps(json_dict, indent=3, ensure_ascii=False)
                    print(new_json)

def get_date_verbose(str_date, limit=0):
    #loading loggs on the screen of a certain date

    logging.basicConfig(level=logging.DEBUG,
                        format="%(levelname)s %(asctime)s - %(message)s")
    logger = logging.getLogger()

    with open("temporary_storage.csv", encoding="utf-8") as r_file:
        count, number = 0, 0
        if limit == None:
            limit = 0
        file_reader = csv.reader(r_file)
        if count < limit:
            for row in file_reader:
                if count < limit:
                    if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and\
                            months[row[2][8:11]] == str_date[4:6]:
                        number += 1
                        logger.debug(f"getting the {number} news from temporary_storage")
                        try:
                            logger.debug(f"getting the feed of the {number} site")
                            title = row[0]
                            logger.debug(f"getting the title of the {number} site")
                            title = row[1]
                            logger.debug(f"getting the pubDate of the {number} site")
                            title = row[2]
                            logger.debug(f"getting the link of the {number} site")
                            title = row[3]
                            logger.debug(f"getting the description of the {number} site\n")
                            title = row[4]
                        except AttributeError:
                            logger.error("'NoneType' object has no attribute 'text'")
                        count += 1
        else:
            for row in file_reader:
                if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and \
                        months[row[2][8:11]] == str_date[4:6]:
                    number += 1
                    logger.debug(f"parsing the {number} news")
                    try:
                        logger.debug(f"getting the feed of the {number} site")
                        title = row[0]
                        logger.debug(f"getting the title of the {number} site")
                        title = row[1]
                        logger.debug(f"getting the pubDate of the {number} site")
                        title = row[2]
                        logger.debug(f"getting the link of the {number} site")
                        title = row[3]
                        logger.debug(f"getting the description of the {number} site\n")
                        title = row[4]
                    except AttributeError:
                        logger.error("'NoneType' object has no attribute 'text'")

def convert_news_in_pdf_date(str_date, limit=0):
    # upload to the screen the news by a certain date in the format in pdf
    with open("temporary_storage.csv", encoding="utf-8") as r_file:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        count = 0
        if limit == None:
            limit = 0
        file_reader = csv.reader(r_file)
        if count < limit:
            for row in file_reader:
                if count < limit:
                    if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and\
                            months[row[2][8:11]] == str_date[4:6]:
                        n = 2
                        pdf.cell(0, 10, txt=f"Feed: {row[0]}", ln=1)
                        pdf.cell(0, 5, txt=f"Title: {row[1]}", ln=1)
                        pdf.cell(0, 5, txt=f"PubDate: {row[2]}", ln=1)
                        pdf.cell(0, 5, txt=f"Link: {row[3]}", ln=1)
                        pdf.cell(0, 5, txt="Description: " + str(row[4].encode("ascii", "ignore"))[n:70], ln=1)
                        n += 69

                        for new_line in range(math.ceil(len(row[4]) / 69)):
                            pdf.cell(0, 5, txt=str(row[4].encode("ascii", "ignore"))[n:69 + n], ln=1)
                            n += 69
                        count += 1

        else:
            for row in file_reader:
                if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and\
                        months[row[2][8:11]] == str_date[4:6]:
                    n = 2
                    pdf.cell(0, 10, txt=f"Feed: {row[0]}", ln=1)
                    pdf.cell(0, 5, txt=f"Title: {row[1]}", ln=1)
                    pdf.cell(0, 5, txt=f"PubDate: {row[2]}", ln=1)
                    pdf.cell(0, 5, txt=f"Link: {row[3]}", ln=1)
                    pdf.cell(0, 5, txt="Description: " + str(row[4].encode("ascii", "ignore"))[n:70], ln=1)
                    n += 69

                    for new_line in range(math.ceil(len(row[4]) / 69)):
                        pdf.cell(0, 5, txt=str(row[4].encode("ascii", "ignore"))[n:69 + n], ln=1)
                        n += 69
        pdf.output("newsPDF.pdf")

def convert_news_in_epub_date(str_date, limit=0):
    # upload to the screen the news by a certain date in the format in epub
    with open("temporary_storage.csv", encoding="utf-8") as r_file:
        if limit == None:
            limit = 0
        temporarily_content = ""
        book = epub.EpubBook()
        book.set_identifier('id1')
        book.set_title('NewsEPUB')
        book.add_author('Evgeny Bykov')
        c1 = epub.EpubHtml(title='newsEPUB', file_name='chap.xhtml')
        count = 0
        file_reader = csv.reader(r_file)
        if count < limit:
            for row in file_reader:
                if count < limit:
                    if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and\
                            months[row[2][8:11]] == str_date[4:6]:
                        c1_content = f"<p>{row[0]}</p><p>Title: {row[1]} </p>" \
                                     f"<p>Date: {row[2]}</p>" \
                                     f"<p>Link: {row[3]}</p>" \
                                     f"<p>{row[4]}</p>"
                        temporarily_content += c1_content
                        count += 1

        else:
            for row in file_reader:
                if row[2][5:7] == str_date[6:8] and row[2][12:16] == str_date[:4] and\
                        months[row[2][8:11]] == str_date[4:6]:
                    c1_content = f"<p>{row[0]}</p><p>Title: {row[1]} </p>" \
                                 f"<p>Date: {row[2]}</p>" \
                                 f"<p>Link: {row[3]}</p>" \
                                 f"<p>{row[4]}</p>"
                    temporarily_content += c1_content

        c1.content = temporarily_content
        book.add_item(c1)
        book.toc = epub.Section('newsEPUB'), c1
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        epub.write_epub('newsEPUB.epub', book, {})


