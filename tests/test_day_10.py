from day_10 import look_and_say


def test_look_and_say():
    assert look_and_say("1") == "11"
    assert look_and_say("11") == "21"
    assert look_and_say("21") == "1211"
    assert look_and_say("1211") == "111221"
    assert look_and_say("111221") == "312211"
    assert look_and_say("1", 1) == "11"
    assert look_and_say("1", 2) == "21"
    assert look_and_say("1", 3) == "1211"
    assert look_and_say("1", 4) == "111221"
    assert look_and_say("1", 5) == "312211"
