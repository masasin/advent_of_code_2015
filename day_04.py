"""
http://adventofcode.com/day/4

--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

    - If your secret key is abcdef, the answer is 609043, because the MD5 hash
      of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the
      lowest such number to do so.
    - If your secret key is pqrstuv, the lowest number it combines with to make
      an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
      pqrstuv1048970 looks like 000006136ef....

--- Part Two ---

Now find one that starts with six zeroes.

"""
from hashlib import md5
from itertools import count


def test_get_hash():
    assert get_hash("abcdef", 609043) == "000001dbbfa3a5c83a2d506429c7b00e"
    assert get_hash("pqrstuv", 1048970) == "000006136ef2ff3b291c85725f17325c"


def test_find_smallest_int():
    assert find_smallest_int("abcdef") == 609043
    assert find_smallest_int("pqrstuv") == 1048970


def get_hash(string, number):
    md5_input = "{string}{number}".format(string=string, number=number).encode()
    return md5(md5_input).hexdigest()


def find_smallest_int(string, n_leading_zeros=5):
    for number in count(1):
        md5_hash = get_hash(string, number)
        if md5_hash.startswith("0" * n_leading_zeros):
            return number


def part_one():
    with open("inputs/day_04_input.txt", "r") as input_file:
        print("Smallest positive number: {}".format(
            find_smallest_int(input_file.read().strip())))


def part_two():
    with open("inputs/day_04_input.txt", "r") as input_file:
        print("Smallest positive number: {}".format(
            find_smallest_int(input_file.read().strip(), 6)))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
