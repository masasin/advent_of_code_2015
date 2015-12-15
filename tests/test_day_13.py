from itertools import permutations

from day_13 import Arranger


inputs = ("Alice would gain 54 happiness units by sitting next to Bob.\n"
          "Alice would lose 79 happiness units by sitting next to Carol.\n"
          "Alice would lose 2 happiness units by sitting next to David.\n"
          "Bob would gain 83 happiness units by sitting next to Alice.\n"
          "Bob would lose 7 happiness units by sitting next to Carol.\n"
          "Bob would lose 63 happiness units by sitting next to David.\n"
          "Carol would lose 62 happiness units by sitting next to Alice.\n"
          "Carol would gain 60 happiness units by sitting next to Bob.\n"
          "Carol would gain 55 happiness units by sitting next to David.\n"
          "David would gain 46 happiness units by sitting next to Alice.\n"
          "David would lose 7 happiness units by sitting next to Bob.\n"
          "David would gain 41 happiness units by sitting next to Carol.")


def test_parse():
    gain = "Alice would gain 54 happiness units by sitting next to Bob."
    lose = "Alice would lose 79 happiness units by sitting next to Carol."
    arranger = Arranger()
    arranger.parse(gain + "\n" + lose)
    assert arranger.potentials == {("Alice", "Bob"): 54,
                                   ("Alice", "Carol"): -79}


def test_pair_happiness():
    arranger = Arranger()
    arranger.potentials = {("Alice", "Bob"): 54,
                           ("Bob", "Alice"): 83}
    assert arranger.pair_happiness("Alice", "Bob") == 54 + 83


def test_arrangement_happiness():
    arranger = Arranger()
    arranger.parse(inputs)
    arranger.arrangement_happiness(["Alice", "Bob", "Carol", "David"]) == 330


def test_get_attendees():
    arranger = Arranger()
    arranger.parse(inputs)
    assert arranger.get_attendees() == {"Alice", "Bob", "Carol", "David"}


def test_get_best_score():
    arranger = Arranger()
    arranger.parse(inputs)
    assert arranger.get_best_score() == 330


def test_get_best_score_not_circular():
    arranger = Arranger()
    arranger.parse(inputs)
    assert arranger.get_best_score(circular=False) == 286
