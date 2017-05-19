"""."""


import pytest


TEST_ITER = [
    ('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
    ('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']),
    ([1, 2, 2, 3, 3], [1, 2, 3]),
    ('James Feore', ['J', 'a', 'm', 'e', 's', 'F', 'o', 'r']),
    ([-1, -2, -3, -4, -3, -2, -1], [-1, -2, -3, -4])
]


@pytest.mark.parametrize('list, result', TEST_ITER)
def test_unique_in_order(iterable, result):
    """."""
    from unique import unique_in_order
    assert unique_in_order(iterable) == result
