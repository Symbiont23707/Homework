class Counter:
    """Counter class which optionally accepts the start value and the counter stop value"""
    count = 0
    def __init__(self, start=0, stop=None):
        self.stop = stop
        self.start = start
        self.current = start

    def increment(self):
        if self.stop is None or self.current < self.stop:
            self.current += 1

        else:
            print("Maximal value is reached.")

    def get(self):
        print(self.current)

c = Counter(start=42, stop=43)
c.increment()
c.get()

c.increment()
c.get()



