"""Kata: Unique In Order.

Take a string and return a list of each unique char in that string, in order

#1 Best Practices Solution by kmeshu09, others

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
"""


def unique_in_order(iterable):
    """."""
    if not iterable:
        return []
    new_list = [iterable[0]]
    for ind in range(len(iterable)):
        if new_list[len(new_list) - 1] != iterable[ind]:
            new_list.append(iterable[ind])
    return new_list
