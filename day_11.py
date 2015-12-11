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


def test_find_next_password():
    assert find_next_password("abcdefgh") == "abcdffaa"
    assert find_next_password("ghijklmn") == "ghjaabcc"


def find_next_password(password, n=1):
    for i in range(n):
        password = increment_password(password)
        while not validate(password):
            password = increment_password(password)
    return password


def validate(password):
    # Requirement 2
    if re.search(r"[iol]", password):
        return False

    # Requirement 1
    for i in range(len(password) - 2):
        if password[i:i+3] in ascii_lowercase:
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


def main():
    with open("inputs/day_11_input.txt") as fin:
        password = fin.readline().strip()
    next_password = find_next_password(password)
    print("Next password: {}".format(next_password))
    print("Next next password: {}".format(find_next_password(next_password)))


if __name__ == "__main__":
    main()
