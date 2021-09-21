original_list = [1, 2, 3, 4, 5]
def foo(original_list: list[int]) -> list[int]:
    """function which, given a list of integers, return a new list such that each element at index i of the new list is the product of all the numbers in the original array except the one at i"""
    multiply = 1
    multiply_list = []
    for i in range(0, len(original_list), 1):
        for x in range(0, len(original_list), 1):
            if i != x:
                multiply *= original_list[x]
        multiply_list.append(multiply)
        multiply = 1
    return multiply_list
print(foo(original_list))
print(foo([3, 2, 1]))