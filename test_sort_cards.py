"""Test sort_cards.py."""


import pytest


TEST_CARDS = [
    (list('39A5T824Q7J6K'), list('A23456789TJQK')),
    (list('Q286JK395A47T'), list('A23456789TJQK')),
    (list('54TQKJ69327A8'), list('A23456789TJQK')),
    ('A', ['A']),
    ('3', ['3']),
    ('T', ['T']),
    (['T', '8', '2', '4', 'Q'], list('248TQ')),
    (['Q', 'K', 'J', '6', '9', '3', '2'], list('2369JQK')),
    (['5', 'Q', '2', '6', '9', '2', '5', 'K', '3', '7'], list('22355679QK'))
]


@pytest.mark.parametrize('iter, result', TEST_CARDS)
def test_sort_cards(iter, result):
    """Return a sorted list of cards."""
    from sort_cards import sort_cards
    assert sort_cards(iter) == result
