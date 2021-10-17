import argparse
class Argsparse_rss:


    def arser_argsparse(self):

        parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")

        parser.add_argument("--version", help="Print version info", action="version", version='"Version 2.0"')
        parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
        parser.add_argument("--verbose", help="Outputs verbose status messages", action="store_true")
        parser.add_argument("--limit", action='store', type=int, help="Limit news topics if this parameter provided",
                            const=0, nargs="?")
        parser.add_argument("--date", action='store', type=str, help="Limit news topics if this parameter provided",
                            const=0, nargs="?")

        parser.add_argument("source", nargs='?', help="RSS URL")

        args = parser.parse_args()

        return args.source, args.limit, args.json, args.verbose, args.date


