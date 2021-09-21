dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
def combine_dicts(*args) -> dict:
    """function, that receives changeable number of dictionaries and combines them into one dictionary."""
    final_dict = args[0]
    for i in args[1:]:
        for key in i.keys():
            if key in final_dict:
                final_dict[key] += i[key]
            else:
                final_dict[key] = i[key]
    return final_dict
print(combine_dicts(dict_1,dict_2,dict_3))