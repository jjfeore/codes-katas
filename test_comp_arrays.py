"""."""


import pytest


TEST_COMP = [
    ([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361], True),
    ([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25], True),
    ([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361], False),
    ([0, 4, 0, 0], [0, 0, 0, 16], True),
    ([-1, -2, -3, -4], [1, 9, 4, 16], True),
    ([-1, 2, -3, 4], [1, 5, 7, 9], False),
    ([20, 30, 40], [400, 1600, 900], True),
    ([], [], True),
    ([], [1, 2, 3], False),
    ([1, 2, 3], None, False)
]


@pytest.mark.parametrize('arr1, arr2, result', TEST_COMP)
def test_comp(arr1, arr2, result):
    """."""
    from comp_arrays import comp
    assert comp(arr1, arr2) == result
