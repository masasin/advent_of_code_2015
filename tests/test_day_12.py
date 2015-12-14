from day_12 import sum_non_reds, sum_numbers


def test_sum_numbers():
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers({"a": 2, "b": 4}) == 6
    assert sum_numbers([[[3]]]) == 3
    assert sum_numbers({"a": {"b": 4}, "c": -1}) == 3
    assert sum_numbers({"a": [-1, 1]}) == 0
    assert sum_numbers([-1, {"a": 1}]) == 0
    assert sum_numbers([]) == 0
    assert sum_numbers({}) == 0


def test_sum_non_reds():
    assert sum_non_reds([1, 2, 3]) == 6
    assert sum_non_reds([1, {"c": "red", "b": 2}, 3]) == 4
    assert sum_non_reds({"d": "red", "e": [1, 2, 3, 4], "f": 5}) == 0
    assert sum_non_reds({"d": "red", "e": [1, 2, {}, 3, 4], "f": 5}) == 0
    assert sum_non_reds([1, "red", 5]) == 6
