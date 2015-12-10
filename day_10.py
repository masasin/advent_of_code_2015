from itertools import groupby


def test_iterate():
    assert iterate("1") == "11"
    assert iterate("11") == "21"
    assert iterate("21") == "1211"
    assert iterate("1211") == "111221"
    assert iterate("111221") == "312211"


def test_iterate_count():
    assert iterate("1", 1) == "11"
    assert iterate("1", 2) == "21"
    assert iterate("1", 3) == "1211"
    assert iterate("1", 4) == "111221"
    assert iterate("1", 5) == "312211"


def iterate(n, count=1):
    for _ in range(count):
        n = "".join(str(len(list(g))) + str(k) for k, g in groupby(n))
    return n


def part_one():
    with open("inputs/day_10_input.txt") as fin:
        number = fin.readline().strip()
    print(len(iterate(number, 40)))


def part_two():
    with open("inputs/day_10_input.txt") as fin:
        number = fin.readline().strip()
    print(len(iterate(number, 50)))


if __name__ == "__main__":
    part_one()
    part_two()
