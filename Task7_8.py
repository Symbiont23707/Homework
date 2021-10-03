class MySquareIterator:
    def __init__(self, lst: list):
        self.lst = lst

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        try:
            self.index += 1
            return self.lst[self.index] ** 2
        except IndexError:
            raise StopIteration

def main():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=" ")
if __name__ == "__main__":
    main()