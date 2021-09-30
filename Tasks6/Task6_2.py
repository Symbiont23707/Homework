class HistoryDict:
    """custom dictionary that will memorize 10 latest changed keys"""
    def __init__(self, old_dict):
        self.old_dict = old_dict
        self.historydict = dict()

    def set_value(self, key, value):
        if len(self.historydict) < 10:
            self.historydict[key] = value
        else:
            print("Your dictionary is already full")

    def get_history(self):
        if len(self.historydict) == 0:
            print("Your dictionary is empty")
        else:
            print(list(self.historydict.keys()))
            self.old_dict = self.historydict
            self.historydict.clear()

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()


