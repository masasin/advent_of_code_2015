from itertools import tee
import re
from string import ascii_lowercase


def test_validate():
    assert validate("hijklmmn") is False
    assert validate("abbceffg") is False
    assert validate("abbcejgk") is False
    assert validate("abcdffaa")
    assert validate("ghjaabcc")


def test_increment_password():
    assert increment_password("xx") == "xy"
    assert increment_password("xy") == "xz"
    assert increment_password("xz") == "ya"
    assert increment_password("ya") == "yb"
    assert increment_password("abcdefgh") == "abcdefgi"
    assert increment_password("abcdefgz") == "abcdefha"
    assert increment_password("abczzzzz") == "abdaaaaa"


def test_next_letter():
    assert next_letter("a") == "b"
    assert next_letter("k") == "l"
    assert next_letter("z") == "a"


def test_window():
    assert list(window("abcd")) == [("a", "b"), ("b", "c"), ("c", "d")]
    assert list(window("abcd", 3)) == [("a", "b", "c"), ("b", "c", "d")]


def test_find_next_password():
    assert find_next_password("abcdefgh") == "abcdffaa"
    assert find_next_password("ghijklmn") == "ghjaabcc"


def window(iterable, size=2):
    splits = list(tee(iterable, size))
    for i, t in enumerate(splits):
        for _ in range(i):
            next(t)
    return zip(*splits)


def find_next_password(password, n=1):
    for i in range(n):
        password = increment_password(password)
        while not validate(password):
            password = increment_password(password)
    return password


def validate(password):
    # Requirement 2
    bad_letters = ("iol")
    for letter in bad_letters:
        if letter in password:
            return False

    # Requirement 1
    for i in window(ascii_lowercase, 3):
        if "".join(i) in password:
            break
    else:
        return False

    # Requirement 3
    return True if re.search(r"(\w)\1.*(\w)\2", password) else False


def increment_password(password):
    if password.endswith("z"):
        i_z = password.index("z")
        n_z = len(password) - i_z
        boundary_letter = password[i_z - 1]
        return password[:i_z - 1] + next_letter(boundary_letter) + "a" * n_z
    else:
        return password[:-1] + next_letter(password[-1])


def next_letter(c):
    try:
        return ascii_lowercase[ascii_lowercase.index(c) + 1]
    except IndexError:  # z
        return "a"


def part_one():
    with open("inputs/day_11_input.txt") as fin:
        password = fin.readline().strip()
    print("Next password: {}".format(find_next_password(password)))


def part_two():
    with open("inputs/day_11_input.txt") as fin:
        password = fin.readline().strip()
    print("Next password: {}".format(find_next_password(password, 2)))


if __name__ == "__main__":
    part_one()
    part_two()
