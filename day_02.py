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


def test_get_get_surface_area():
    assert get_surface_area([2, 3, 4]) == 52
    assert get_surface_area([1, 1, 10]) == 42


def test_get_slack():
    assert get_slack([2, 3, 4]) == 6
    assert get_slack([1, 1, 10]) == 1


def test_get_total_area():
    assert get_total_area("2x3x4") == 58
    assert get_total_area("1x1x10") == 43


def test_get_dimensions():
    assert get_dimensions("2x3x4") == [2, 3, 4]
    assert get_dimensions("1x1x10") == [1, 1, 10]
    assert get_dimensions("5x4x3") == [3, 4, 5]


def test_get_shortest_perimeter():
    assert get_shortest_perimeter([2, 3, 4]) == 10
    assert get_shortest_perimeter([1, 1, 10]) == 4


def test_get_volume():
    assert get_volume([2, 3, 4]) == 24
    assert get_volume([1, 1, 10]) == 10


def test_get_ribbon_length():
    assert get_ribbon_length("2x3x4") == 34
    assert get_ribbon_length("1x1x10") == 14


def get_surface_area(dimensions):
    l, w, h = dimensions
    return 2*l*w + 2*w*h + 2*l*h


def get_volume(dimensions):
    l, w, h = dimensions
    return l * h * w


def get_slack(dimensions):
    return dimensions[0] * dimensions[1]


def get_shortest_perimeter(dimensions):
    return 2 * (dimensions[0] + dimensions[1])


def get_total_area(box_size):
    dimensions = get_dimensions(box_size)
    return get_surface_area(dimensions) + get_slack(dimensions)


def get_ribbon_length(box_size):
    dimensions = get_dimensions(box_size)
    return get_volume(dimensions) + get_shortest_perimeter(dimensions)


def get_dimensions(box_size):
    return sorted(int(i) for i in box_size.split("x"))


def part_one():
    with open("inputs/day_02_input.txt", "r") as input_file:
        total_area = 0
        for box_dims in input_file:
            total_area += get_total_area(box_dims)
        print("Total area: {} square feet".format(total_area))


def part_two():
    with open("inputs/day_02_input.txt", "r") as input_file:
        total_length = 0
        for box_dims in input_file:
            total_length += get_ribbon_length(box_dims)
        print("Total ribbon length: {} feet".format(total_length))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
