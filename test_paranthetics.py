"""Test paranthetics.py."""


import pytest


TEST_PARENS = [
    ('((()))', 0),
    (')))(((', -1),
    ('(()', 1),
    ('()))', -1),
    (')(((', -1),
    ('())(', -1),
    ('()(', 1),
    ('', 0)
]


@pytest.mark.parametrize('str, result', TEST_PARENS)
def test_check_parens(str, result):
    """Return 0 for a balanced str, 1 for an open one, and -1 for broken."""
    from paranthetics import check_parens
    assert check_parens(str) == result
