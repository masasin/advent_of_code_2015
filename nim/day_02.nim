import algorithm
import future
import strutils


proc parse*(size: string): seq[int] =
  sorted(lc[parseInt(i) | (i <- size.split('x')), int], system.cmp[int])


proc get_total_area*(size: string): int =
  var
    sides = parse(size)
    width = sides[0]
    height = sides[1]
    length = sides[2]
  2 * (length * width + width * height + height * length) + width * height


proc get_ribbon_length*(size: string): int =
  var
    sides = parse(size)
    width = sides[0]
    height = sides[1]
    length = sides[2]
  length * width * height + 2 * (width + height)


proc part_one(input: string) =
  var total_area = 0
  for size in input.strip().splitlines():
    total_area += get_total_area(size)
  echo "Total area: ", total_area, " square feet"


proc part_two(input: string) =
  var total_length = 0
  for size in input.strip().splitlines():
    total_length += get_ribbon_length(size)
  echo "Total length: ", total_length, " feet"


when isMainModule:
  let input = readFile("inputs/day_02_input.txt")
  part_one(input)
  part_two(input)
