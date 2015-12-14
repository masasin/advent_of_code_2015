import numpy as np

from day_06 import parse_instruction, follow_instruction, follow_elvish


def test_parse_instruction():
    assert parse_instruction("turn on 0,0 through 999,999") == (
        "turn on",
        slice(0, 1000),
        slice(0, 1000),
    )
    assert parse_instruction("toggle 0,0 through 999,0") == (
        "toggle",
        slice(0, 1000),
        slice(0, 1),
    )
    assert parse_instruction("turn off 499,499 through 500,500") == (
        "turn off",
        slice(499, 501),
        slice(499, 501),
    )


def test_follow_instruction():
    orig_array = np.zeros((1000, 1000))
    true_array = np.ones((1000, 1000))
    new_array = follow_instruction("turn on 0,0 through 999,999", orig_array)
    assert new_array.all()
    new_array = follow_instruction("turn on 0,0 through 999,999", true_array)
    assert new_array.all()

    orig_array = np.zeros((1000, 1000))
    true_array = np.ones((1000, 1000))
    new_array = follow_instruction("turn off 499,499 through 500,500",
                                   orig_array)
    assert not new_array[499:500, 499:500].any()
    new_array = follow_instruction("turn off 499,499 through 500,500",
                                   true_array)
    assert not new_array[499:500, 499:500].any()

    orig_array = np.zeros((1000, 1000))
    true_array = np.ones((1000, 1000))
    new_array = follow_instruction("toggle 499,499 through 500,500", orig_array)
    assert new_array[499:500, 499:500].all()
    new_array = follow_instruction("toggle 499,499 through 500,500", true_array)
    assert not new_array[499:500, 499:500].any()

    orig_array = np.zeros((1000, 1000))
    true_array = np.ones((1000, 1000))
    new_array = follow_instruction("toggle 0,0 through 999,0", orig_array)
    assert new_array[:, 0].all()
    new_array = follow_instruction("toggle 0,0 through 999,0", true_array)
    assert not new_array[:, 0].any()


def test_follow_elvish():
    orig_array = np.zeros((1000, 1000))
    new_array = follow_elvish("turn off 499,499 through 500,500", orig_array)
    assert new_array.sum() == 0
    orig_array = np.zeros((1000, 1000))
    new_array = follow_elvish("turn on 499,499 through 500,500", orig_array)
    assert new_array.sum() == 4
    orig_array = np.zeros((1000, 1000))
    new_array = follow_elvish("toggle 499,499 through 500,500", orig_array)
    assert new_array.sum() == 8
    orig_array = np.zeros((1000, 1000))
    new_array = follow_elvish("turn on 0,0 through 0,0", orig_array)
    assert new_array.sum() == 1
    orig_array = np.zeros((1000, 1000))
    new_array = follow_elvish("toggle 0,0 through 999,999", orig_array)
    assert new_array.sum() == 2000000
