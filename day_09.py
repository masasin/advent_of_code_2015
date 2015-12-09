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
