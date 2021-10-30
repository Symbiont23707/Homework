
from rss_packaging.argparse_rss import Argsparse_rss
from rss_packaging.rss_read import Rss_reader


def main():
    start_argparse = Argsparse_rss()
    source = start_argparse.arser_argsparse()[0]
    limit = start_argparse.arser_argsparse()[1]

    A = Rss_reader(source, limit)


    if start_argparse.arser_argsparse()[3]:
        A.reader_rss_with_loggs()
    elif start_argparse.arser_argsparse()[2]:
        A.reader_rss_with_json_format()
    else:
        A.reader_rss()


if __name__ == "__main__":
    main()
