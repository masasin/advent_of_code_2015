"""
http://adventofcode.com/day/10

--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has
devised a method of coming up with a password based on the previous one.
Corporate policy dictates that passwords must be exactly eight lowercase letters
(for security reasons), so he finds his new password by incrementing his old
password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on.
Increase the rightmost letter one step; if it was z, it wraps around to a, and
repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed
some additional password requirements:

    - Passwords must include one increasing straight of at least three letters,
      like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd
      doesn't count.
    - Passwords may not contain the letters i, o, or l, as these letters can be
      mistaken for other characters and are therefore confusing.
    - Passwords must contain at least two different, non-overlapping pairs of
      letters, like aa, bb, or zz.

For example:

    - hijklmmn meets the first requirement (because it contains the straight
      hij) but fails the second requirement (because it contains i and l).
    - abbceffg meets the third requirement (because it repeats bb and ff) but
      fails the first requirement.
    - abbcegjk fails the third requirement, because it only has one double
      letter (bb).
    - The next password after abcdefgh is abcdffaa.
    - The next password after ghijklmn is ghjaabcc, because you eventually skip
      all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next
password be?

--- Part Two ---

Santa's password expired again. What's the next one?

"""
import re
from string import ascii_lowercase


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
