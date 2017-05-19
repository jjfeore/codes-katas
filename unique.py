"""."""


def unique_in_order(iterable):
    """."""
    if not iterable:
        return []
    new_list = [iterable[0]]
    for ind in range(len(iterable)):
        if new_list[len(new_list) - 1] != iterable[ind]:
            new_list.append(iterable[ind])
    return new_list
