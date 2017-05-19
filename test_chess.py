"""."""


import pytest


TEST_CHESS = [
    ("A1", "C3", True),
    ("A1", "H3", False),
    ("A1", "A2", False),
    ("A1", "A3", True),
    ("B3", "C2", True),
    ("D5", "E6", True),
    ("B3", "C5", False)
]


TEST_LETTER = [
    ("A", 0),
    ("a", 0),
    ("E", 0),
    ("B", 1),
    ("D", 1),
    ("b", 1)
]


@pytest.mark.parametrize('c1, c2, result', TEST_CHESS)
def test_chess_board_cell_color(c1, c2, result):
    """."""
    from chess import chess_board_cell_color
    assert chess_board_cell_color(c1, c2) == result


@pytest.mark.parametrize('letter, result', TEST_LETTER)
def test_check_letter(letter, result):
    """."""
    from chess import check_letter
    assert check_letter(letter) == result
