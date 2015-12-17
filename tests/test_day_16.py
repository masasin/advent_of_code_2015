from day_16 import parse, matches, real_matches, results


def test_parse():
    assert parse("Sue 1: cars: 9, akitas: 3, goldfish: 0") == {
        "cars": 9,
        "akitas": 3,
        "goldfish": 0
    }


def test_matches():
    assert not matches({"cars": 9, "akitas": 3, "goldfish": 0}, results)
    assert not matches({"cars": 9, "akitas": 0, "goldfish": 0}, results)
    assert not matches({"cars": 9, "akitas": 3, "goldfish": 5}, results)
    assert not matches({"cars": 2, "akitas": 3, "goldfish": 0}, results)
    assert matches({"cars": 2, "akitas": 0, "goldfish": 5}, results)


def test_real_matches():
    assert not real_matches({"pomeranians": 3, "perfumes": 1, "vizslas": 0},
                            results)
    assert real_matches({"goldfish": 0, "vizslas": 0, "samoyeds": 2}, results)
