"""."""


import pytest


TEST_SPLIT = [
    ('James Feore', ['Ja', 'me', 's ', 'Fe', 'or', 'e_']),
    ('ABBCcAD', ['AB', 'BC', 'cA', 'D_']),
    ('1234', ['12', '34']),
    ('multiple words', ['mu', 'lt', 'ip', 'le', ' w', 'or', 'ds']),
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"])
]


@pytest.mark.parametrize('s, result', TEST_SPLIT)
def test_solution(s, result):
    """."""
    from split_strings import solution
    assert solution(s) == result
