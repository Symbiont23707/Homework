def sort_file():
    """function which sorts the names and write them to a new file"""
    with open('data/unsorted_names.txt', 'r') as unsorted_f,\
        open('data/sorted_names.txt', 'w') as sorted_f:
        sorted_f.writelines(sorted(unsorted_f.readlines()))
    print(sort_file())