print("Task 1.4:") #для удобства в проверке
dict1 = {4: "apple", 1: "orange", 2: "pineapple", 5: "pear"}
def sort_dictionary_by_key(dict1):
    saved_items = dict1.items()
    dict1 = sorted(saved_items)
    return dict(dict1)
print(sort_dictionary_by_key(dict1))