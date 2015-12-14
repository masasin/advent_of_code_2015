import pytest

from day_11 import validate, increment_password, next_letter, find_next_password


def test_validate():
    assert validate("hijklmmn") is False
    assert validate("abbceffg") is False
    assert validate("abbcejgk") is False
    assert validate("abcdffaa")
    assert validate("ghjaabcc")


def test_increment_password():
    assert increment_password("xx") == "xy"
    assert increment_password("xy") == "xz"
    assert increment_password("xz") == "ya"
    assert increment_password("ya") == "yb"
    assert increment_password("abcdefgh") == "abcdefgi"
    assert increment_password("abcdefgz") == "abcdefha"
    assert increment_password("abczzzzz") == "abdaaaaa"


def test_next_letter():
    assert next_letter("a") == "b"
    assert next_letter("k") == "l"
    assert next_letter("z") == "a"


@pytest.skip
def test_find_next_password():
    assert find_next_password("abcdefgh") == "abcdffaa"
    assert find_next_password("ghijklmn") == "ghjaabcc"
