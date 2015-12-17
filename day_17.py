"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all
into your refrigerator, you'll need to move it into smaller containers. You take
an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If
you need to store 25 liters, there are four ways to do it:

    - 15 and 10
    - 20 and 5 (the first 5)
    - 20 and 5 (the second 5)
    - 15, 5, and 5

Filling all containers entirely, how many different combinations of containers
can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen, another load of eggnog
arrives! The shipping and receiving department is requesting as many containers
as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of
eggnog. How many different ways can you fill that number of containers and still
hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three
ways to use that many containers, and so the answer there would be 3.

"""
from itertools import combinations


def parse(stream):
    return sorted(int(i) for i in stream.strip().split("\n"))


def find_combos(target, sizes):
    return list(combo for n_containers in range(1, len(sizes) + 1)
                for combo in combinations(sizes, n_containers)
                if sum(combo) == target)


def find_n_combos(target, sizes):
    return len(find_combos(target, sizes))


def find_min_combos(target, sizes):
    combos = find_combos(target, sizes)
    return sum(1 for combo in combos if len(combo) == len(combos[0]))


def part_one():
    with open("inputs/day_17_input.txt") as fin:
        sizes = parse(fin.read())
    print("{} total combinations".format(find_n_combos(150, sizes)))


def part_two():
    with open("inputs/day_17_input.txt") as fin:
        sizes = parse(fin.read())
    print("{} minimal combinations".format(find_min_combos(150, sizes)))


if __name__ == "__main__":
    part_one()
    part_two()
