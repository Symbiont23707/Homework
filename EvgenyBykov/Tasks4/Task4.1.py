### Task 4.1
text = "s asdasd asdas das \" \' sada \"  \" \""
def replaces_symbols2(text):
    """ function which receives a string and replaces all " symbols with ' and vise versa."""
    return text.replace("\"", "\'", text.count("\"")) + "\n" + text.replace("\'", "\"", text.count("\'"))
print(replaces_symbols2(text))