import csv

def get_top_performers(file_path, number_of_top_students=5):
    """function which receives file path and returns names of top performer students"""
    with open(file_path, "r") as file:
        list_of_data, name_list = [], []
        file_r = csv.reader(file)
        header = next(file)
        for data in file_r:
            list_of_data.append(data)
        list_of_data.sort(key=lambda k: float(k[2]), reverse=True)
        for name in list_of_data[:number_of_top_students]:
            name_list.append(name[0])
        return name_list

def get_top_age(file_path, sorted_by_age):
    """function which writes CSV student information to the new file in descending order of age"""
    with open(file_path, "r") as file_r, open(sorted_by_age, "w", newline='\n') as file_w:
        list_of_data, name_list = [], []
        file_read = csv.reader(file_r)
        for data in file_read:
            list_of_data.append(data)
        list_of_data.sort(key=lambda k: k[1], reverse=True)
        file_write = csv.writer(file_w)
        file_write.writerows(list_of_data)

print(get_top_performers(".//data/students.csv"))
print(get_top_age(".//data/students.csv", ".//data/sorted_by_age"))