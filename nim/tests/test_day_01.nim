import unittest

import "../day_01"


suite "Day 1 tests":
  test "d01: Get the floor Santa ends up on":
    check:
      get_floor("(())") == 0
      get_floor("()()") == 0
      get_floor("(()(()(") == 3
      get_floor("(((") == 3
      get_floor("))(((((") == 3
      get_floor("))(") == -1
      get_floor("())") == -1
      get_floor(")())())") == -3
      get_floor(")))") == -3

  test "d01: Get the first step where Santa enters the basement":
    check:
      get_first_basement_step(")") == 1
      get_first_basement_step("()())") == 5
