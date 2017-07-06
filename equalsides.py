"""Kata: Equal Sides Of An Array.

Find the index of an array where the sum of the values on each side are equal

#1 Best Practices Solution by CrazyMerlyn, Ales Akulchyk, danthemantran, others

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
"""


def find_even_index(arr):
    """."""
    left = []
    right = []
    for i in range(len(arr)):
        left.append(sum(arr[:i + 1]))
        right.append(sum(arr[i:]))
        if left[i] == right[i]:
            return i
    return -1
