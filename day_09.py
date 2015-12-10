"""
http://adventofcode.com/day/9

--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided
him the distances between every pair of locations. He can start and end at any
two (different) locations he wants, but he must visit each location exactly
once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

    - London to Dublin = 464
    - London to Belfast = 518
    - Dublin to Belfast = 141

The possible routes are therefore:

    - Dublin -> London -> Belfast = 982
    - London -> Dublin -> Belfast = 605
    - London -> Belfast -> Dublin = 659
    - Dublin -> Belfast -> London = 659
    - Belfast -> Dublin -> London = 605
    - Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is
605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the
longest distance instead.

He can still start and end at any two (different) locations he wants, and he
still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for
example) Dublin -> London -> Belfast.

What is the distance of the longest route?

"""
from itertools import permutations, tee
import re


def test_find_shortest_route_length():
    distances = {("London", "Dublin"): 464,
                 ("London", "Belfast"): 518,
                 ("Dublin", "Belfast"): 141}
    for k, v in distances.copy().items():
        distances[tuple(k[::-1])] = v
    assert find_shortest_route_length(distances) == 605


def test_parse():
    assert parse("Snowdin to Tambi = 22") == (("Snowdin", "Tambi"), 22)


def test_add_to_dict():
    d = {}
    add_to_dict((("Snowdin", "Tambi"), 22), d)
    assert d == {("Snowdin", "Tambi"): 22,
                 ("Tambi", "Snowdin"): 22}


def parse(string):
    result = re.search(r"(\w+) to (\w+) = (\d+)", string)
    origin, destination, distance = result.groups()
    return ((origin, destination), float(distance))


def add_to_dict(path, d):
    d[path[0]] = path[1]
    d[tuple(path[0][::-1])] = path[1]


def find_routes(d):
    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    locations = set()
    for k in d.keys():
        locations.add(k[0])
        locations.add(k[1])

    routes = {}
    for route in permutations(locations):
        distance = 0
        for origin, destination in pairwise(route):
            distance += d[(origin, destination)]
        routes[route] = distance
    return routes


def find_shortest_route_length(d):
    routes = find_routes(d)
    return min(routes.values())


def find_longest_route_length(d):
    routes = find_routes(d)
    return max(routes.values())


def part_one():
    with open("inputs/day_09_input.txt") as input_file:
        distances = {}
        for line in input_file.readlines():
            path = parse(line)
            add_to_dict(path, distances)
        print("Shortest route length: {}".format(
            find_shortest_route_length(distances)))


def part_two():
    with open("inputs/day_09_input.txt") as input_file:
        distances = {}
        for line in input_file.readlines():
            path = parse(line)
            add_to_dict(path, distances)
        print("Longest route length: {}".format(
            find_longest_route_length(distances)))


if __name__ == "__main__":
    part_one()
    part_two()
