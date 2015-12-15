from day_15 import parse, score, generate_combos


def test_parse():
    butterscotch = ("Butterscotch: capacity -1, durability -2, flavor 6, "
                    "texture 3, calories 8")
    cinnamon = ("Cinnamon: capacity 2, durability 3, flavor -2, texture -1, "
                "calories 3")
    assert parse(butterscotch) == ("Butterscotch", -1, -2, 6, 3, 8)
    assert parse(cinnamon) == ("Cinnamon", 2, 3, -2, -1, 3)


def test_score():
    ingredients = {"Butterscotch": (-1, -2, 6, 3, 8),
                   "Cinnamon": (2, 3, -2, -1, 3)}

    amounts = {"Butterscotch": 44, "Cinnamon": 56}
    assert score(ingredients, amounts) == 62842880

    amounts = {"Butterscotch": 80, "Cinnamon": 20}
    assert score(ingredients, amounts) == 0


def test_generate_combos():
    assert list(generate_combos(3, 5)) == [(0, 0, 5), (0, 1, 4), (0, 2, 3),
                                           (0, 3, 2), (0, 4, 1), (0, 5, 0),
                                           (1, 0, 4), (1, 1, 3), (1, 2, 2),
                                           (1, 3, 1), (1, 4, 0), (2, 0, 3),
                                           (2, 1, 2), (2, 2, 1), (2, 3, 0),
                                           (3, 0, 2), (3, 1, 1), (3, 2, 0),
                                           (4, 0, 1), (4, 1, 0), (5, 0, 0)]
