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

