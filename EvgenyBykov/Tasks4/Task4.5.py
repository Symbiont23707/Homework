num = 87178291199
def get_digits(num: int) -> tuple[int]:
    """function which returns a tuple of a given integer's digits."""
    tuple_of_digits = [int(i) for i in str(num)]
    return tuple(tuple_of_digits)
print(get_digits(num))