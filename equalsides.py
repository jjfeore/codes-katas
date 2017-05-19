"""."""


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
