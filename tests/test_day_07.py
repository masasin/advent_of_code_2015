import numpy as np
import pytest

from day_07 import Solver


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
