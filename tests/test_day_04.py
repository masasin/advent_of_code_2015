from day_04 import get_hash, find_smallest_int


def test_get_hash():
    assert get_hash("abcdef", 609043) == "000001dbbfa3a5c83a2d506429c7b00e"
    assert get_hash("pqrstuv", 1048970) == "000006136ef2ff3b291c85725f17325c"


def test_find_smallest_int():
    assert find_smallest_int("abcdef", starting_number=609040) == 609043
    assert find_smallest_int("pqrstuv", starting_number=1048960) == 1048970
