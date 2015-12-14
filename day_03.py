"""
http://adventofcode.com/day/3

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his
new location.

However, the elf back at the north pole has had a little too much eggnog, and so
his directions are a little off, and Santa ends up visiting some houses more
than once. How many houses receive at least one present?

For example:

    - > delivers presents to 2 houses: one at the starting location, and one to
      the east.
    - ^>v< delivers presents to 4 houses in a square, including twice to the
      house at his starting/ending location.
    - ^v^v^v^v^v delivers a bunch of presents to some very lucky children at
      only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of
himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the
same starting house), then take turns moving based on instructions from the elf,
who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    - ^v delivers presents to 3 houses, because Santa goes north, and then
      Robo-Santa goes south.
    - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up
      back where they started.
    - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one
      direction and Robo-Santa going the other.

"""


def move(step, coord):
    moves = {
        ">": [1, 0],
        "<": [-1, 0],
        "^": [0, 1],
        "v": [0, -1],
    }

    diff = moves[step]
    return coord[0] + diff[0], coord[1] + diff[1]


def get_visits(steps, n_movers=1):
    visited = {(0, 0)}

    coords = [(0, 0)] * n_movers
    for n_steps, step in enumerate(steps):
        idx = n_steps % n_movers
        coords[idx] = move(step, coords[idx])
        visited.add(coords[idx])

    return len(visited)


def part_one():
    with open("inputs/day_03_input.txt", "r") as input_file:
        print("{} houses visited".format(get_visits(input_file.read())))


def part_two():
    with open("inputs/day_03_input.txt", "r") as input_file:
        print("{} houses visited".format(get_visits(input_file.read(), 2)))


if __name__ == "__main__":
    part_one()
    part_two()
