lst = [1, 2, 3, 8, 9]
def get_pairs(lst: list) -> list[tuple]:
    """function which returns a list of tuples containing pairs of elements."""
    pairs_list = []
    if len(lst) == 1 or len(lst) == 0:
        return None
    for i in range(0,len(lst)-1,1):
        temporarily_tuple = (lst[i], lst[i+1])
        pairs_list.append(temporarily_tuple)
    return pairs_list
print(get_pairs(lst))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))