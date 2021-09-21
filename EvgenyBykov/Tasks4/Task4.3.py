str = "This is my text !"
def split(str, sep = " "):
    """ function which works the same as str.split method """
    temporarily_str = ""
    final_list = []
    str = str.strip(sep)
    str = str + sep
    for i in str:
        if i != sep:
            temporarily_str += i
        else:
            final_list.append(temporarily_str)
            temporarily_str = ""
    return final_list
print(split(str))
print(split("This,is,my,text,!", ","))