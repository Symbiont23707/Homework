print("Task 1.6:") #для удобства в проверке
def multiplication_table(a = 2,b = 4,c = 3,d = 7):
    for x in range(c, d + 1):
        if x == c:
            print("    "+str(x), end="   ")
        else:
            print(str(x), end="   ")
    print(sep="\n")
    for i in range(a, b+1):
        list3 = []
        print(i, end="   ")
        for x in range(c, d+1):
            list3.append(i*x)
        for row in list3:
            if row > 9:
                print(row, end="  ")
            else:
                print(row, end="   ")
        print(sep="\n")
multiplication_table()
