"""Kata: Chess Fun #1: Chess Board Cell Color.

Check if two squares from a chess board are the same color

#1 Best Practices Solution by daddepledge

def chess_board_cell_color(a, b):
    return (ord(a[0]) + int(a[1])) % 2 == (ord(b[0]) + int(b[1])) % 2
"""


def chess_board_cell_color(cell1, cell2):
    """."""
    check1 = check_letter(cell1[0])
    check2 = check_letter(cell2[0])
    yaxis1 = int(cell1[1]) % 2
    yaxis2 = int(cell2[1]) % 2
    check1 += yaxis1
    check2 += yaxis2
    if check1 == check2 or abs(check1 - 2) == check2:
        return True
    else:
        return False


def check_letter(letter):
    """."""
    letter = letter.upper()
    if letter in 'BDFH':
        return 1
    else:
        return 0
