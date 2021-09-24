def most_common_words(filepath, number_of_words=3):
    """function which search for most common words in the file"""
    all_words_in_file = dict()
    with open(filepath, "r") as file:
       content = file.read()
       for words in content.lower().replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").split():
           if words in all_words_in_file.keys():
               all_words_in_file[words] += 1
           else:
               all_words_in_file[words] = 1
    all_words_in_file = list({k: v for k, v in sorted(all_words_in_file.items(), key=lambda v: v[1], reverse=True)})[:number_of_words]
    return all_words_in_file
print(most_common_words("..//Tasks5/data/lorem_ipsum.txt"))
