s = "pythoniscool,isn'tit?"
indexes = [6, 8, 12, 13, 18]
def split_by_index(s: str, indexes: list[int]) -> list[str]:
    """ function which splits the `s` string by indexes specified in `indexes`."""
    edited_list = []
    n = 0
    if indexes[-1] > len(s):
        return [s]
    for index in indexes:
        text = s[n:index]
        n = index
        edited_list.append(text)
    if len(s) == n:
        return edited_list
    edited_list.append(s[n:])
    return edited_list
print(split_by_index(s,indexes))