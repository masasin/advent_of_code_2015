import unittest

import "../day_02"


suite "Day 2 tests":
  test "d02: Parse an input line":
    check:
      parse("2x3x4") == @[2, 3, 4]
      parse("1x1x10") == @[1, 1, 10]
      parse("5x4x3") == @[3, 4, 5]

  test "d02: Get total area":
    check:
      get_total_area("2x3x4") == 58
      get_total_area("1x1x10") == 43

  test "d02: Get ribbon length":
    check:
      get_ribbon_length("2x3x4") == 34
      get_ribbon_length("1x1x10") == 14
