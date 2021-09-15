print("Task 1.2:") #для удобства в проверке

str2 = "Oh, it is python"
def number_of_characters(str2):
    characters_and_count = {}
    for i in str2.lower():
        characters_and_count[i] = str2.count(i)
    return characters_and_count
print(number_of_characters(str2)) #для удобства в проверке