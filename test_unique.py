"""."""


import pytest


TEST_ITER = [
    ('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
    ('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']),
    ([1, 2, 2, 3, 3], [1, 2, 3]),
    ('Hello!', ['H', 'e', 'l', 'o', '!']),
    ('YYzzyyZZDDDDDDDD', ['Y', 'z', 'y', 'Z', 'D']),
    ([-1, -2, -3, -4, -3, -2, -1], [-1, -2, -3, -4, -3, -2, -1])
]


@pytest.mark.parametrize('iterable, result', TEST_ITER)
def test_unique_in_order(iterable, result):
    """."""
    from unique import unique_in_order
    assert unique_in_order(iterable) == result
