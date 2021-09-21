import string
test = ["hello", "world", "python", ]
def test_1_1(*args) -> set:
    """function which returns characters that appear in all strings"""
    set_result = set(args[0])
    final_set = set()
    count = 0
    for char in set_result:
        for word in args[1:]:
            if char in word:
                count += 1
        if count == len(args)-1:
            final_set.add(char)
        count = 0
    return final_set
print(test_1_1(*test))

def test_1_2(*args) -> set:
    """function which returns characters that appear in at least one string"""
    all_letters_in_args = set()
    for word in args:
        all_letters_in_args = set.union(all_letters_in_args,set(word))
    return all_letters_in_args
print(test_1_2(*test))

def test_1_3(*args) -> set:
    """function which returns characters that appear at least in two strings"""
    set_two_repeats_times = set()
    all_letters = test_1_2(*args)
    count = 0
    for char in all_letters:
        for word in args:
            if char in word:
                count += 1
            if count >= 2:
                set_two_repeats_times.add(char)
        count = 0
    return set_two_repeats_times
print(test_1_3(*test))

def test_1_4(*args) -> set:
    """function which returns characters of alphabet, that were not used in any string"""
    all_letters = test_1_2(*args)
    letter_that_not_used = set(string.ascii_lowercase) - all_letters
    return letter_that_not_used
print(test_1_4(*test))