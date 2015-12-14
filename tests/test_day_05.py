from day_05 import is_nice_1, is_nice_2


def test_naughty_or_nice_1():
    assert is_nice_1("ugknbfddgicrmopn")
    assert is_nice_1("aaa")
    assert is_nice_1("aeicc")
    assert is_nice_1("xazeggov")
    assert is_nice_1("aeiouaaeiouaeiou")
    assert is_nice_1("baccedee")
    assert is_nice_1("bbaaccedde")
    assert not is_nice_1("jchzalnrumimnmhp")
    assert not is_nice_1("haegwjzuvuyypxyu")
    assert not is_nice_1("dvszwmarrgswjxmb")


def test_naughty_or_nice_2():
    assert is_nice_2("xyxy")
    assert is_nice_2("aabcdefegaa")
    assert is_nice_2("abcdefeghicd")
    assert is_nice_2("aaabcdab")
    assert is_nice_2("qjhvhtzxzqqjkmpb")
    assert is_nice_2("xxyxx")
    assert not is_nice_2("aaa")
    assert not is_nice_2("uurcxstgmygtbstg")
    assert not is_nice_2("ieodomkazucvgmuy")


