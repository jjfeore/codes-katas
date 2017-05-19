"""."""


def comp(array1, array2):
    """."""
    if array1 and array2:
        true = 0
        for num in array1:
            if (num ** 2) in array2:
                true += 1
        if true == len(array1):
            return True
    return False
