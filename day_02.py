"""
http://adventofcode.com/day/2

--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order
for more. They have a list of the dimensions (length l, width w, and height h)
of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which
makes calculating the required wrapping paper for each gift a little easier:
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also
need a little extra paper for each present: the area of the smallest side.

For example:

    - A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square
      feet of wrapping paper plus 6 square feet of slack, for a total of 58
      square feet.
    - A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square
      feet of wrapping paper plus 1 square foot of slack, for a total of 43
      square feet.

All numbers in the elves' list are in feet. How many total square feet of
wrapping paper should they order?

--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they
only have to worry about the length they need to order, which they would again
like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides,
or the smallest perimeter of any one face. Each present also requires a bow made
out of ribbon as well; the feet of ribbon required for the perfect bow is equal
to the cubic feet of volume of the present. Don't ask how they tie the bow,
though; they'll never tell.

For example:

    - A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to
      wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total
      of 34 feet.
    - A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to
      wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total
      of 14 feet.

How many total feet of ribbon should they order?

"""


def parse(box_size):
    """
    Return the dimensions of the box.

    Parameters
    ----------
    box_size : str
        The size of the box, represented as axbxc, where a, b, and c are the
        lengths of one side of the box, in feet.

    Returns
    -------
    3-tuple of float
        The lengths of each side of the box, from smallest to largest.

    """
    return sorted(int(i) for i in box_size.split("x"))


def get_total_area(box_size):
    """
    Return the total area of wrapping paper required.

    Parameters
    ----------
    box_size : str
        The size of the box, represented as axbxc, where a, b, and c are the
        lengths of one side of the box, in feet.

    Returns
    -------
    float
        The total area of wrapping paper required, in square feet.

    """
    w, h, l = parse(box_size)
    return 2 * (l*w + w*h + h*l) + w*h


def get_ribbon_length(box_size):
    """
    Return the total length of ribbon required.

    Parameters
    ----------
    box_size : str
        The size of the box, represented as axbxc, where a, b, and c are the
        lengths of one side of the box, in feet.

    Returns
    -------
    float
        The total length of ribbon required, in feet.

    """
    w, h, l = parse(box_size)
    return l*w*h + 2 * (w + h)


def part_one():
    """
    Solve Part 1.

    """
    with open("inputs/day_02_input.txt", "r") as input_file:
        total_area = 0
        for box_dims in input_file:
            total_area += get_total_area(box_dims)
        print("Total area: {} square feet".format(total_area))


def part_two():
    """
    Solve Part 2.

    """
    with open("inputs/day_02_input.txt", "r") as input_file:
        total_length = 0
        for box_dims in input_file:
            total_length += get_ribbon_length(box_dims)
        print("Total ribbon length: {} feet".format(total_length))


if __name__ == "__main__":
    part_one()
    part_two()
