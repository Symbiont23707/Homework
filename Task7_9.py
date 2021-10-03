class EvenRange:
    """iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even
     numbers during iteration"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if self.start % 2 != 0:
            self.current_number = self.start + 1
        else:
            self.current_number = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number < self.end:
            result = self.current_number
            self.current_number += 2
            return result
        else:
            """If user tries to iterate after it gave all possible numbers Out of numbers! should be printed."""
            print('"Out of numbers!"')
            raise StopIteration



def main():
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    #print(next(er1))
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number, end=" ")

if __name__ == "__main__":
    main()