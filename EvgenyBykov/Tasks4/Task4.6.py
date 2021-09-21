s = "Python is simple and effective!"
def get_longest_word(s: str) -> str:
    """function which returns the longest word in the given string."""
    len_of_str, max_len = 0, 0
    temporarily_str = ""
    for char in s:
        if char != " " and char != "\n" and char != "\t":
            temporarily_str += char
            len_of_str += 1
        else:
            if max_len < len_of_str:
                max_len = len_of_str
                max_str = temporarily_str
            len_of_str = 0
            temporarily_str = ""
    if len_of_str > max_len:
        max_str = temporarily_str

    return max_str
print(get_longest_word(s))
####################### or ######################
def get_longest_word2(s: str) -> str:
    """function which returns the longest word in the given string."""
    list_str = []
    max_len = 0
    list_str = s.split()
    for i in list_str:
        if len(i) > max_len:
            max_len = len(i)
            biggest_str = i
    return biggest_str
print(get_longest_word2(s))