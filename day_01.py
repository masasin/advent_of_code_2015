"""
http://adventofcode.com/day/1

--- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas, but his weather machine's "snow"
function is powered by stars, and he's fresh out! To save Christmas, he needs
you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available
on each day in the advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't
find the right floor - the directions he got are a little confusing. He starts
on the ground floor (floor 0) and then follows the instructions one character at
a time.

An opening parenthesis, (, means he should go up one floor, and a closing
parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will
never find the top or bottom floors.

For example:

    - (()) and ()() both result in floor 0.
    - ((( and (()(()( both result in floor 3.
    - ))((((( also results in floor 3.
    - ()) and ))( both result in floor -1 (the first basement level).
    - ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?)

--- Part Two ---

Now, given the same instructions, find the position of the first character that
causes him to enter the basement (floor -1). The first character in the
instructions has position 1, the second character has position 2, and so on.

For example:

    - ) causes him to enter the basement at character position 1.
    - ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the
basement?

"""


def test_get_floor():
    assert get_floor("()()") == 0
    assert get_floor("(((") == 3
    assert get_floor("))(((((") == 3
    assert get_floor("())") == -1
    assert get_floor(")))") == -3


def get_floor(directions):
    """
    Get the floor for Santa.

    Parameters
    ----------
    directions : str
        A string of parentheses representing directions. An opening parenthesis,
        (, means he should go up one floor, and a closing parenthesis, ), means
        he should go down one floor.

    Returns
    -------
    int
        The floor to which Santa should go.

    Examples
    --------
    >>> get_floor("(())")
    0
    >>> get_floor("(()(()(")
    3
    >>> get_floor("))(")
    -1
    >>> get_floor(")())())")
    -3

    """
    floor = 0
    for step in directions:
        floor += {"(": 1, ")": -1}[step]
    return floor


def get_first_basement_step(directions):
    """
    Get the first step where Santa goes into the basement.

    Parameters
    ----------
    directions : str
        A string of parentheses representing directions. An opening parenthesis,
        (, means he should go up one floor, and a closing parenthesis, ), means
        he should go down one floor.

    Returns
    -------
    int
        The first step where Santa goes into the basement.

    Examples
    --------
    >>> get_first_basement_step(")")
    1
    >>> get_first_basement_step("()())")
    5

    """
    floor = 0

    for current_step, step in enumerate(directions, 1):
        floor += {"(": 1, ")": -1}[step]
        if floor == -1:
            return current_step


def one_function():
    """
    Solve the full problem.

    """
    with open("inputs/day_01_input.txt", "r") as input_file:
        directions = input_file.read()

    floor = 0
    passed_basement = False

    for i, step in enumerate(directions, 1):
        floor += {"(": 1, ")": -1}[step]
        if not passed_basement and floor == -1:
            print("Basement on step {}".format(i))
            passed_basement = True
    print("Go to floor {}".format(floor))


def part_one():
    """
    Solve Part 1.

    """
    with open("inputs/day_01_input.txt", "r") as input_file:
        print("Go to floor {}".format(get_floor(input_file.read())))


def part_two():
    """
    Solve Part 2.

    """
    with open("inputs/day_01_input.txt", "r") as input_file:
        print("Basement on step {}".format(
            get_first_basement_step(input_file.read())))


if __name__ == "__main__":
    part_one()
    part_two()
