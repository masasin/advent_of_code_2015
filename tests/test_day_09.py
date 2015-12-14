from day_09 import (find_shortest_route_length, find_longest_route_length,
                    parse, add_to_dict)


def test_find_shortest_route_length():
    distances = {("London", "Dublin"): 464,
                 ("London", "Belfast"): 518,
                 ("Dublin", "Belfast"): 141}
    for k, v in distances.copy().items():
        distances[tuple(k[::-1])] = v
    assert find_shortest_route_length(distances) == 605


def test_find_longest_route_length():
    distances = {("London", "Dublin"): 464,
                 ("London", "Belfast"): 518,
                 ("Dublin", "Belfast"): 141}
    for k, v in distances.copy().items():
        distances[tuple(k[::-1])] = v
    assert find_longest_route_length(distances) == 982


def test_parse():
    assert parse("Snowdin to Tambi = 22") == (("Snowdin", "Tambi"), 22)


def test_add_to_dict():
    d = {}
    add_to_dict((("Snowdin", "Tambi"), 22), d)
    assert d == {("Snowdin", "Tambi"): 22,
                 ("Tambi", "Snowdin"): 22}
