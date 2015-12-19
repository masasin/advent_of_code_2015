from day_19 import (parse, count_molecules, steps_to_generate, reverse_dict,
                    generate_prev)


def test_parse():
    stream = "H => HO\nH => OH\nO => HH\n\nHOH\n"
    assert parse(stream) == ({"H": ["HO", "OH"], "O": ["HH"]}, "HOH")
    assert parse(stream.strip()) == ({"H": ["HO", "OH"], "O": ["HH"]}, "HOH")


def test_count_molecules():
    replacements = {"H": ["HO", "OH"], "O": ["HH"], "Al": ["C"]}
    assert count_molecules("HOH", replacements) == 4
    assert count_molecules("HOHOHO", replacements) == 7
    assert count_molecules("HOHC", replacements) == 4
    assert count_molecules("AlHOH", replacements) == 5
    assert count_molecules("HOAlH", replacements) == 6


def test_steps_to_generate():
    replacements = {"e": ["H", "O"], "H": ["HO", "OH"], "O": ["HH"]}
    assert steps_to_generate("HOH", replacements) == 3
    assert steps_to_generate("HOHOHO", replacements) == 6


def test_reverse_dict():
    replacements = {"e": ["H", "O"], "H": ["HO", "OH"], "O": ["HH"]}
    assert reverse_dict(replacements) == {"H": ["e"], "O": ["e"],
                                          "HO": ["H"], "OH": ["H"],
                                          "HH": ["O"]}


def test_generate_prev():
    replacements = {"e": ["H", "O"], "H": ["HO", "OH"], "O": ["HH"]}
    assert generate_prev("HOH", reverse_dict(replacements)) == {"HH"}
    assert generate_prev("HH", reverse_dict(replacements)) == {"O"}
    assert generate_prev("O", reverse_dict(replacements)) == {"e"}
