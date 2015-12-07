"""
http://adventofcode.com/day/1

--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic
gates! Unfortunately, little Bobby is a little under the recommended age range,
and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit
signal (a number from 0 to 65535). A signal is provided to each wire by a gate,
another wire, or some specific value. Each wire can only get a signal from one
source, but can provide its signal to multiple destinations. A gate provides no
signal until all of its inputs have a signal.

The included instructions booklet describe how to connect the parts together:
x AND y -> z means to connect wires x and y to an AND gate, and then connect its
output to wire z.

For example:

    - 123 -> x means that the signal 123 is provided to wire x.
    - x AND y -> z means that the bitwise AND of wire x and wire y is provided
      to wire z.
    - p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and
      then provided to wire q.
    - NOT e -> f means that the bitwise complement of the value from wire e is
      provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for
some reason, you'd like to emulate the circuit instead, almost all programming
languages (for example, C, JavaScript, or Python) provide operators for these
gates.

For example, here is a simple circuit:

    - 123 -> x
    - 456 -> y
    - x AND y -> d
    - x OR y -> e
    - x LSHIFT 2 -> f
    - y RSHIFT 2 -> g
    - NOT x -> h
    - NOT y -> i

After it is run, these are the signals on the wires:

    - d: 72
    - e: 507
    - f: 492
    - g: 114
    - h: 65412
    - i: 65079
    - x: 123
    - y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input),
what signal is ultimately provided to wire a?

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and
reset the other wires (including wire a). What new signal is ultimately provided
to wire a?

"""
import operator

import numpy as np
import pytest


def test_parse():
    solver = Solver()
    solver.parse("123 -> x")
    assert solver.inputs == {"x": "123".split()}

    solver = Solver()
    solver.parse("456 -> y")
    assert solver.inputs == {"y": "456".split()}

    solver = Solver()
    solver.parse("123 AND 456 -> x")
    assert solver.inputs == {"x": "123 AND 456".split()}

    solver = Solver()
    solver.parse("x AND 456 -> z")
    assert solver.inputs == {"z": "x AND 456".split()}

    solver = Solver()
    solver.parse("NOT 123 -> y")
    assert solver.inputs == {"y": "NOT 123".split()}


def test_make_outputs():
    solver = Solver()
    solver.parse("123 -> x")
    solver.make_outputs()
    assert solver.outputs == {"x": 123}

    solver = Solver()
    solver.parse("456 -> y")
    solver.make_outputs()
    assert solver.outputs == {"y": 456}

    solver = Solver()
    solver.parse("123 AND 456 -> x")
    solver.make_outputs()
    assert solver.outputs == {"x": 123 & 456}

    solver = Solver()
    solver.parse("NOT 123 -> y")
    solver.make_outputs()
    assert solver.outputs == {"y": ~np.uint16(123)}


def test_do_instruction():
    solver = Solver()
    solver.inputs = {"x": "123", "y": "456"}
    solver.outputs = {"x": 123, "y": 456}

    assert solver.do_instruction(["123"]) == 123
    assert solver.do_instruction(["456"]) == 456
    assert solver.do_instruction("123 AND 456".split()) == 123 & 456
    assert solver.do_instruction("NOT 123".split()) == ~np.uint16(123)
    assert solver.do_instruction(["x"]) == 123
    assert solver.do_instruction(["y"]) == 456
    assert solver.do_instruction("x AND y".split()) == 123 & 456
    assert solver.do_instruction("123 AND y".split()) == 123 & 456
    assert solver.do_instruction("x AND 456".split()) == 123 & 456
    assert solver.do_instruction("NOT x".split()) == ~np.uint16(123)


def test_get_value():
    solver = Solver()
    with pytest.raises(ValueError):
        solver.get_value("x")
    solver.inputs = {"x": ["123"], "y": "x AND 119".split()}
    with pytest.raises(KeyError):
        solver.get_value("x")
    solver.outputs = {"x": 123, "y": 115}
    assert solver.get_value("y") == 115
    assert solver.get_value("115") == 115


def test_make_inputs():
    string = "123 -> x\n456 -> y"
    solver = Solver()
    solver.make_inputs(string)
    assert solver.inputs == {"x": ["123"], "y": ["456"]}

    string = "123 -> y\ny -> x"
    solver = Solver()
    solver.make_inputs(string)
    assert solver.inputs == {"x": ["y"], "y": ["123"]}


def test_solve():
    string = "123 -> x\n456 -> y"
    solver = Solver()
    solver.solve(string)
    assert solver.outputs == {"x": 123, "y": 456}

    string = "123 -> y\ny -> x"
    solver = Solver()
    solver.solve(string)
    assert solver.outputs == {"x": 123, "y": 123}

    string = "\n".join(("123 -> x",
                        "456 -> y",
                        "x AND y -> d",
                        "x OR y -> e",
                        "x LSHIFT 2 -> f",
                        "y RSHIFT 2 -> g",
                        "NOT x -> h",
                        "NOT y -> i",))

    solver = Solver()
    solver.solve(string)
    assert solver.outputs == {"d": 72,
                              "e": 507,
                              "f": 492,
                              "g": 114,
                              "h": 65412,
                              "i": 65079,
                              "x": 123,
                              "y": 456}

    string = "\n".join(("123 -> x",
                        "x AND y -> d",
                        "x OR y -> e",
                        "x LSHIFT 2 -> f",
                        "456 -> y",
                        "y RSHIFT 2 -> g",
                        "NOT x -> h",
                        "NOT y -> i",))
    solver = Solver()
    solver.solve(string)
    assert solver.outputs == {"d": 72,
                              "e": 507,
                              "f": 492,
                              "g": 114,
                              "h": 65412,
                              "i": 65079,
                              "x": 123,
                              "y": 456}


class Solver(object):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

    def solve(self, instructions):
        self.make_inputs(instructions)
        self.make_outputs()

    def make_inputs(self, instructions):
        for instruction in instructions.splitlines():
            self.parse(instruction)

    def parse(self, instruction):
        (ops, wire) = instruction.split(" -> ")
        self.inputs[wire] = ops.split()

    def make_outputs(self):
        keys = set(self.inputs.keys())
        while keys:
            for key in keys.copy():
                try:
                    self.outputs[key] = self.do_instruction(self.inputs[key])
                    keys.remove(key)
                except KeyError:
                    continue

    def do_instruction(self, instruction):
        if len(instruction) == 1:
            return self.get_value(instruction[0])
        elif len(instruction) == 2:
            return ~self.get_value(instruction[1])
        elif len(instruction) == 3:
            operations = {
                "AND": operator.and_,
                "OR": operator.or_,
                "LSHIFT": operator.lshift,
                "RSHIFT": operator.rshift,
            }

            in_1 = self.get_value(instruction[0])
            op = instruction[1]
            in_2 = self.get_value(instruction[2])
            return operations[op](in_1, in_2)

    def get_value(self, item):
        if item in self.inputs:
            return np.uint16(self.outputs[item])
        else:
            return np.uint16(item)


def part_one():
    solver = Solver()
    with open("inputs/day_07_input.txt") as input_file:
        solver.solve(input_file.read())
    print("Wire a: {}".format(solver.outputs["a"]))


def part_two():
    with open("inputs/day_07_input.txt") as input_file:
        input_text = input_file.read()

    solver = Solver()
    solver.solve(input_text)
    a_value = solver.outputs["a"]

    modified_solver = Solver()
    modified_solver.make_inputs(input_text)
    modified_solver.inputs["b"] = [str(a_value)]
    modified_solver.make_outputs()
    new_a_value = modified_solver.outputs["a"]
    print("New wire a: {}".format(new_a_value))


if __name__ == "__main__":
    part_one()
    part_two()
