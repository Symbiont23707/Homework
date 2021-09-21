number = 5
def generate_squares(number: int) -> dict:
    """function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number."""
    return {num: num*num for num in range(1, number+1, 1)}
print(generate_squares(number))

