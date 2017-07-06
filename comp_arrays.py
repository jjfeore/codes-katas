"""Kata: Are they the "same"? - Check if one array is the square of another.

#1 Best Practices Solution by macintosh95, punk_ist, noelleon

def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
"""


def comp(array1, array2):
    """."""
    if array1 is not None and array2 is not None and len(array1) == len(array2):
        true = 0
        for num in array1:
            if (num ** 2) in array2:
                true += 1
                array2.remove(num ** 2)
        if true == len(array1) and not array2:
            return True
    return False
