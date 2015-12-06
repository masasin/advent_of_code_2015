"""
http://adventofcode.com/day/6

--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to
9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
doing the instructions Santa sent you in order.

For example:

    - turn on 0,0 through 999,999 would turn on (or leave on) every light.
    - toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
      turning off the ones that were on, and turning on the ones that were off.
    - turn off 499,499 through 500,500 would turn off (or leave off) the middle
      four lights.

After following the instructions, how many lights are lit?

--- Part Two ---

You just finish implementing your winning light pattern when you realize you
mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each
light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of
those lights by 1.

The phrase turn off actually means that you should decrease the brightness of
those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of
those lights by 2.

What is the total brightness of all lights combined after following Santa's
instructions?

For example:

    - turn on 0,0 through 0,0 would increase the total brightness by 1.
    - toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""
import re


PATTERN = re.compile(r"([\w\s]+)\s(\d+),(\d+) through (\d+),(\d+)")


def test_interpret_instruction():
    assert interpret_instruction("turn on 0,0 through 999,999") == (
        "turn on",
        [0, 0],
        [999, 999],
    )
    assert interpret_instruction("toggle 0,0 through 999,0") == (
        "toggle",
        [0, 0],
        [999, 0],
    )
    assert interpret_instruction("turn off 499,499 through 500,500") == (
        "turn off",
        [499, 499],
        [500, 500],
    )


def test_follow_instruction():
    orig_array = [[False]*1000 for _ in range(1000)]
    true_array = [[True]*1000 for _ in range(1000)]

    new_array = follow_instruction("turn on 0,0 through 999,999", orig_array)
    assert all(new_array)
    new_array = follow_instruction("turn on 0,0 through 999,999", true_array)
    assert all(new_array)

    new_array = follow_instruction("turn off 499,499 through 500,500",
                                   orig_array)
    assert not new_array[499][499]
    assert not new_array[499][500]
    assert not new_array[500][499]
    assert not new_array[500][500]
    new_array = follow_instruction("turn off 499,499 through 500,500",
                                   true_array)
    assert not new_array[499][499]
    assert not new_array[499][500]
    assert not new_array[500][499]
    assert not new_array[500][500]

    new_array = follow_instruction("toggle 499,499 through 500,500", orig_array)
    assert new_array[499][499]
    assert new_array[499][500]
    assert new_array[500][499]
    new_array = follow_instruction("toggle 499,499 through 500,500", true_array)
    assert not new_array[499][499]
    assert not new_array[499][500]
    assert not new_array[500][499]
    assert not new_array[500][500]

    new_array = follow_instruction("toggle 0,0 through 999,0", orig_array)
    assert all([row[0] for row in new_array])
    new_array = follow_instruction("toggle 0,0 through 999,0", true_array)
    assert not any([row[0] for row in new_array])


def test_follow_elvish():
    orig_array = [[0]*1000 for _ in range(1000)]

    new_array = follow_elvish("turn off 499,499 through 500,500", orig_array)
    assert sum(i for row in new_array for i in row) == 0
    new_array = follow_elvish("turn on 499,499 through 500,500", orig_array)
    assert sum(i for row in new_array for i in row) == 4
    new_array = follow_elvish("toggle 499,499 through 500,500", orig_array)
    assert sum(i for row in new_array for i in row) == 8
    new_array = follow_elvish("turn on 0,0 through 0,0", orig_array)
    assert sum(i for row in new_array for i in row) == 1
    new_array = follow_elvish("toggle 0,0 through 999,999", orig_array)
    assert sum(i for row in new_array for i in row) == 2000000


def interpret_instruction(instruction):
    match = re.search(PATTERN, instruction)
    command, start_x, start_y, end_x, end_y = match.groups()
    return command, [int(start_x), int(start_y)], [int(end_x), int(end_y)]


def follow_instruction(instruction, array):
    command, start, end = interpret_instruction(instruction)
    new_array = [row[:] for row in array]

    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if command == "turn on":
                new_array[i][j] = True
            elif command == "turn off":
                new_array[i][j] = False
            elif command == "toggle":
                new_array[i][j] = not array[i][j]
            else:
                raise ValueError("Unknown input")

    return new_array


def follow_elvish(instruction, array):
    command, start, end = interpret_instruction(instruction)
    new_array = [row[:] for row in array]

    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if command == "turn on":
                new_array[i][j] += 1
            elif command == "turn off":
                new_array[i][j] = max(0, new_array[i][j] - 1)
            elif command == "toggle":
                new_array[i][j] += 2
            else:
                raise ValueError("Unknown input")

    return new_array


def part_one():
    with open("inputs/day_06_input.txt", "r") as input_file:
        array = [[False]*1000 for _ in range(1000)]
        for instruction in input_file:
            array = follow_instruction(instruction, array)

    print("{} lights on".format(sum(i for row in array for i in row)))


def part_two():
    with open("inputs/day_06_input.txt", "r") as input_file:
        array = [[0]*1000 for _ in range(1000)]
        for instruction in input_file:
            array = follow_elvish(instruction, array)

    print("{} total brightness".format(sum(i for row in array for i in row)))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
