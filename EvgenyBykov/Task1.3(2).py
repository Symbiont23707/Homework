print("Task 1.3(2):") #для удобства в проверке
def list_divisors():
    number = int(input("What's number u want: "))
    i = 1
    set1 = set()
    while i <= number:
        if number % i == 0:
            set1.add(i)
        i += 1
    return set1
print(list_divisors())