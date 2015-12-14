from day_01 import get_floor, get_first_basement_step


def test_get_floor():
    assert get_floor("(())") == 0
    assert get_floor("()()") == 0
    assert get_floor("(()(()(") == 3
    assert get_floor("(((") == 3
    assert get_floor("))(((((") == 3
    assert get_floor("))(") == -1
    assert get_floor("())") == -1
    assert get_floor(")())())") == -3
    assert get_floor(")))") == -3


def test_get_first_basement_step():
    assert get_first_basement_step(")") == 1
    assert get_first_basement_step("()())") == 5
