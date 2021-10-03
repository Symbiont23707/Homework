class IsNotEvenError(Exception):
    pass


class NumberLessThanTwo(Exception):
    pass


def number_checker(number):
    """Implement function for check that number is even and is greater than 2. Throw different exceptions for this
    errors. Custom exceptions must be derived from custom base exception(not Base Exception class)."""
    if isinstance(number, int):
        ...
    else:
        raise TypeError("Number is not a int")
    if number % 2 != 0:
        raise IsNotEvenError("Number is not a even")
    if number < 2:
        raise NumberLessThanTwo("Number more than two")


def main():
    number_checker(4)

if __name__ == "__main__":
    main()