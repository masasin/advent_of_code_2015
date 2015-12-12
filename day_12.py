"""
http://adventofcode.com/day/11

--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format. That's
where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]),
objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find
all of the numbers throughout the document and add them together.

For example:

    - [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    - [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    - {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    - [] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything
red.

Ignore any object (and all of its children) which has any property with the
value "red". Do this only for objects {...}), not arrays ([...]).

    - [1,2,3] still has a sum of 6.
    - [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is
      ignored.
    - {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire
      structure is ignored.
    - [1,"red",5] has a sum of 6, because "red" in an array has no effect.

"""
import json
import re


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


def sum_numbers(s):
    return sum(int(i) for i in re.findall(r"(-?\d+)", str(s)))


def sum_non_reds(s):
    if isinstance(s, int):
        return s
    if isinstance(s, list):
        return sum(sum_non_reds(i) for i in s)
    elif isinstance(s, dict):
        if "red" in s.values():
            return 0
        else:
            return sum(sum_non_reds(i) for i in s.values())

    return 0


def part_one():
    with open("inputs/day_12_input.txt") as fin:
        print(sum_numbers(fin.read()))


def part_two():
    with open("inputs/day_12_input.txt") as fin:
        print(sum_non_reds(json.load(fin)))


if __name__ == "__main__":
    part_one()
    part_two()
