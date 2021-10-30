import publishing_date
from rss_packaging.argparse_rss import Argsparse_rss
from rss_packaging.rss_read import Rss_reader


def rss():
    start_argparse = Argsparse_rss()
    source = start_argparse.arser_argsparse()[0]
    limit = start_argparse.arser_argsparse()[1]
    ##--date
    if start_argparse.arser_argsparse()[4]:
        if start_argparse.arser_argsparse()[3]:
            publishing_date.get_date_verbose(start_argparse.arser_argsparse()[4], start_argparse.arser_argsparse()[1])
        elif start_argparse.arser_argsparse()[5] and start_argparse.arser_argsparse()[2]:
            publishing_date.convert_news_in_pdf_date(start_argparse.arser_argsparse()[4],
                                                     start_argparse.arser_argsparse()[1])
            publishing_date.get_date_json(start_argparse.arser_argsparse()[4], start_argparse.arser_argsparse()[1])
        elif start_argparse.arser_argsparse()[6] and start_argparse.arser_argsparse()[2]:
            publishing_date.convert_news_in_epub_date(start_argparse.arser_argsparse()[4],
                                                      start_argparse.arser_argsparse()[1])
            publishing_date.get_date_json(start_argparse.arser_argsparse()[4], start_argparse.arser_argsparse()[1])
        elif start_argparse.arser_argsparse()[6]:
            publishing_date.convert_news_in_epub_date(start_argparse.arser_argsparse()[4],
                                                      start_argparse.arser_argsparse()[1])
        elif start_argparse.arser_argsparse()[5]:
            publishing_date.convert_news_in_pdf_date(start_argparse.arser_argsparse()[4],
                                                     start_argparse.arser_argsparse()[1])
        elif start_argparse.arser_argsparse()[2]:
            publishing_date.get_date_json(start_argparse.arser_argsparse()[4], start_argparse.arser_argsparse()[1])
        else:
            publishing_date.get_date(start_argparse.arser_argsparse()[4], start_argparse.arser_argsparse()[1])

    else:
        A = Rss_reader(source, limit)
        A.content_local_storage()

        if start_argparse.arser_argsparse()[3]:
            A.reader_rss_with_loggs()
        elif start_argparse.arser_argsparse()[5] and start_argparse.arser_argsparse()[2]:
            A.reader_rss_with_json_format()
            A.convert_news_in_pdf()
        elif start_argparse.arser_argsparse()[6] and start_argparse.arser_argsparse()[2]:
            A.reader_rss_with_json_format()
            A.convert_news_in_epub()
        elif start_argparse.arser_argsparse()[6]:
            A.convert_news_in_epub()
        elif start_argparse.arser_argsparse()[5]:
            A.convert_news_in_pdf()
        elif start_argparse.arser_argsparse()[2]:
            A.reader_rss_with_json_format()
        else:
            A.reader_rss()


if __name__ == "__main__":
    rss()
