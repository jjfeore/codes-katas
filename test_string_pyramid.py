"""Tests for string_pyramid.py."""


import pytest


TEST_SIDE = [
    ('abc', '  c  \n bbb \naaaaa'),
    ('aaa', '  a  \n aaa \naaaaa'),
    ('a', 'a'),
    ('', ''),
    (None, None),
    ('ab', ' b \naaa'),
    ('54321', '    1    \n   222   \n  33333  \n 4444444 \n555555555')
]


TEST_VIS = [
    ('abc', 25),
    ('aaa', 25),
    ('a', 1),
    ('', -1),
    (None, -1),
    ('ab', 9),
    ('54321', 81)
]


TEST_ABOVE = [
    ('abc', 'aaaaa\nabbba\nabcba\nabbba\naaaaa'),
    ('aaa', 'aaaaa\naaaaa\naaaaa\naaaaa\naaaaa'),
    ('a', 'a'),
    ('', ''),
    (None, None),
    ('ab', 'aaa\naba\naaa'),
    ('54321', '555555555\n544444445\n543333345\n543222345\n543212345\n543222345\n543333345\n544444445\n555555555')
]


TEST_TOTAL = [
    ('abc', 35),
    ('aaa', 35),
    ('a', 1),
    ('', -1),
    (None, -1),
    ('ab', 10),
    ('54321', 165)
]


@pytest.mark.parametrize('str, result', TEST_SIDE)
def test_watch_from_side(str, result):
    """Return a string pyramid as viewed from the side."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(str) == result


@pytest.mark.parametrize('str, result', TEST_ABOVE)
def test_watch_from_above(str, result):
    """Return a string pyramid as viewed from above."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(str) == result


@pytest.mark.parametrize('str, result', TEST_VIS)
def test_count_visible(str, result):
    """Return the visible number of stones in the pyramid."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid(str) == result


@pytest.mark.parametrize('str, result', TEST_TOTAL)
def test_count_total(str, result):
    """Return the total number of stones in the pyramid."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(str) == result
