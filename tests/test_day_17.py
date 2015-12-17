from day_17 import parse, find_n_combos, find_min_combos


def test_parse():
    assert parse("20\n15\n10\n5\n5") == [5, 5, 10, 15, 20]
    assert parse("10\n15\n20\n5\n5") == [5, 5, 10, 15, 20]


def test_parse_with_empty_line():
    assert parse("20\n15\n10\n5\n5\n") == [5, 5, 10, 15, 20]
    assert parse("10\n15\n20\n5\n5\n") == [5, 5, 10, 15, 20]


def test_find_n_combos():
    assert find_n_combos(25, [5, 5, 10, 15, 20]) == 4


def test_find_min_combos():
    assert find_min_combos(25, [5, 5, 10, 15, 20]) == 3
