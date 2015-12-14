from day_02 import parse, get_total_area, get_ribbon_length


def test_parse():
    assert parse("2x3x4") == [2, 3, 4]
    assert parse("1x1x10") == [1, 1, 10]
    assert parse("5x4x3") == [3, 4, 5]


def test_get_total_area():
    assert get_total_area("2x3x4") == 58
    assert get_total_area("1x1x10") == 43


def test_get_ribbon_length():
    assert get_ribbon_length("2x3x4") == 34
    assert get_ribbon_length("1x1x10") == 14
