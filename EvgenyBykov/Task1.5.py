print("Task 1.5:") #для удобства в проверке
list2 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
def unique_values(list2):
    list2_edited = set()
    for i in list2:
        for value in i.values():
            list2_edited.add(value)
    print(list2_edited)
unique_values(list2)