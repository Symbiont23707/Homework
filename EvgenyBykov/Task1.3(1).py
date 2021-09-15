print("Task 1.3(1):") #для удобства в проверке

list1 = ['red', 'white', 'black', 'red', 'green', 'black']
def unique_words(list1):
    edited_list1 = []
    for i in sorted(set(list1)):
        edited_list1.append(i)
    return edited_list1
print(unique_words(list1))