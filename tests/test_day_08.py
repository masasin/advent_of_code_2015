from day_08 import count_characters, count_encoded, count_literals


def test_count_literals():
    assert count_literals(r'""') == 2
    assert count_literals(r'"abc"') == 5
    assert count_literals(r'"aaa\"aaa"') == 10
    assert count_literals(r'"\x27"') == 6


def test_count_characters():
    assert count_characters(r'""') == 0
    assert count_characters(r'"abc"') == 3
    assert count_characters(r'"aaa\"aaa"') == 7
    assert count_characters(r'"aaa\"aaa\""') == 8
    assert count_characters(r'"\x27"') == 1


def test_count_encoded():
    assert count_encoded(r'""') == 6
    assert count_encoded(r'"abc"') == 9
    assert count_encoded(r'"aaa\"aaa"') == 16
    assert count_encoded(r'"\x27"') == 11
