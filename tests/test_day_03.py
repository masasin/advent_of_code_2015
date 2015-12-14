from day_03 import move, get_visits


def test_move():
    assert move(">", (0, 0)) == (1, 0)
    assert move("<", (0, 0)) == (-1, 0)
    assert move("^", (0, 0)) == (0, 1)
    assert move("v", (0, 0)) == (0, -1)

    step_1 = move("^", (0, 0))
    step_2 = move(">", step_1)
    step_3 = move("v", step_2)
    step_4 = move("<", step_3)

    assert step_1 == (0, 1)
    assert step_2 == (1, 1)
    assert step_3 == (1, 0)
    assert step_4 == (0, 0)


def test_get_visits():
    assert get_visits(">") == 2
    assert get_visits("^>v<") == 4
    assert get_visits("^v^v^v^v^v") == 2
    assert get_visits("^>v<>^") == 4
    assert get_visits(">^^v^<>v") == 5


def test_get_visits_with_robot():
    assert get_visits("^v", 2) == 3
    assert get_visits("^>v<", 2) == 3
    assert get_visits("^v^v^v^v^v", 2) == 11
