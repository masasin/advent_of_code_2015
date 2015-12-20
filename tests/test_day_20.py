from day_20 import get_house_n_gifts


def test_get_first_house_with_n_presents():
    assert get_house_n_gifts(60) == 4
    assert get_house_n_gifts(120) == 6
    assert get_house_n_gifts(70, max_visits=2) == 6
    assert get_house_n_gifts(120, max_visits=2) == 8
