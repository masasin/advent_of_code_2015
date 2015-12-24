import tables


const movements = {'(': 1, ')': -1}.toTable


proc get_floor*(directions: string): int =
  for step in items(directions):
    result += movements[step]


proc get_first_basement_step*(directions: string): int =
  var floor = 0
  for result, step in @directions:
    floor += movements[step]
    if floor == -1:
      return result + 1


proc part_one(input: string) =
  echo "Go to floor ", get_floor(input)


proc part_two(input: string) =
  echo "Basement on step ", get_first_basement_step(input)


when isMainModule:
  let input = readFile("inputs/day_01_input.txt")
  part_one(input)
  part_two(input)
