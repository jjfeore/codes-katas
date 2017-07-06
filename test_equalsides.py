"""."""


import pytest


TEST_EQUAL = [
    ([1, 2, 3, 4, 3, 2, 1], 3),
    ([1, 100, 50, -51, 1, 1], 1),
    ([1, 2, 3, 4, 5, 6], -1),
    ([0, 0, 0, 0, 0], 0),
    ([-1, -2, -3, -4, -3, -2, -1], 3),
    ([10, -80, 10, 10, 15, 35, 20], 6),
    ([20, 10, -80, 10, 10, 15, 35], 0)
]


@pytest.mark.parametrize('list, result', TEST_EQUAL)
def test_find_even_index(list, result):
    """."""
    from equalsides import find_even_index
    assert find_even_index(list) == result
