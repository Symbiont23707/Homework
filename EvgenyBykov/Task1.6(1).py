print("Task 1.6:") #для удобства в проверке
tuple1 = (1, 2, 3, 4)
def convert_tuple_in_integer(tuple1):
    convert_number = ""
    for i in tuple1:
        if i > 0:
            convert_number += str(i)
    return int(convert_number)
print(convert_tuple_in_integer(tuple1))