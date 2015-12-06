"""
http://adventofcode.com/day/5

--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or
nice.

A nice string is one with all of the following properties:

    - It contains at least three vowels (aeiou only), like aei, xazegov, or
      aeiouaeiouaeiou.
    - It contains at least one letter that appears twice in a row, like xx,
      abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    - It does not contain the strings ab, cd, pq, or xy, even if they are part
      of one of the other requirements.

For example:

    - ugknbfddgicrmopn is nice because it has at least three vowels
      (u...i...o...), a double letter (...dd...), and none of the disallowed
      substrings.
    - aaa is nice because it has at least three vowels and a double letter, even
      though the letters used by different rules overlap.
    - jchzalrnumimnmhp is naughty because it has no double letter.
    - haegwjzuvuyypxyu is naughty because it contains the string xy.
    - dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules apply, as
they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    - It contains a pair of any two letters that appears at least twice in the
      string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not
      like aaa (aa, but it overlaps).
    - It contains at least one letter which repeats with exactly one letter
      between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    - qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and
      a letter that repeats with exactly one letter between them (zxz).
    - xxyxx is nice because it has a pair that appears twice and a letter that
      repeats with one between, even though the letters used by each rule
      overlap.
    - uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with
      a single letter between them.
    - ieodomkazucvgmuy is naughty because it has a repeating letter with one
      between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

"""


def test_naughty_or_nice_1():
    assert is_nice_1("ugknbfddgicrmopn")
    assert is_nice_1("aaa")
    assert is_nice_1("aeicc")
    assert is_nice_1("xazeggov")
    assert is_nice_1("aeiouaaeiouaeiou")
    assert is_nice_1("baccedee")
    assert is_nice_1("bbaaccedde")
    assert not is_nice_1("jchzalnrumimnmhp")
    assert not is_nice_1("haegwjzuvuyypxyu")
    assert not is_nice_1("dvszwmarrgswjxmb")


def test_naughty_or_nice_2():
    assert is_nice_2("xyxy")
    assert is_nice_2("aabcdefegaa")
    assert is_nice_2("abcdefeghicd")
    assert is_nice_2("aaabcdab")
    assert is_nice_2("qjhvhtzxzqqjkmpb")
    assert is_nice_2("xxyxx")
    assert not is_nice_2("aaa")
    assert not is_nice_2("uurcxstgmygtbstg")
    assert not is_nice_2("ieodomkazucvgmuy")


def is_nice_1(string):
    bad_substrings = ("ab", "cd", "pq", "xy")
    vowels = "aeiou"
    vowel_count = 0
    has_duplicates = False

    for i in range(len(string) - 1):
        if string[i] in vowels:
            vowel_count += 1

        if string[i] + string[i+1] in bad_substrings:
            return False

        if string[i] == string[i+1]:
            has_duplicates = True
    if string[-1] in vowels:
        vowel_count += 1

    return vowel_count >= 3 and has_duplicates


def is_nice_2(string):
    pairs = {}
    has_duplicate_pair = False
    has_repeating_letter = False

    for i in range(len(string) - 1):
        # Has at least one duplicated pair
        previous_index = pairs.setdefault(string[i] + string[i+1], i)
        if previous_index != i:
            if previous_index != i - 1:
                has_duplicate_pair = True

        # Has repeating letter
        try:
            if string[i] == string[i+2]:
                has_repeating_letter = True
        except IndexError:
            continue

    return has_duplicate_pair and has_repeating_letter


def part_one():
    with open("inputs/day_05_input.txt", "r") as input_file:
        n_nice = 0
        for string in input_file:
            if is_nice_1(string):
                n_nice += 1

    print("{} nice strings".format(n_nice))


def part_two():
    with open("inputs/day_05_input.txt", "r") as input_file:
        n_nice = 0
        for string in input_file:
            if is_nice_2(string):
                n_nice += 1

    print("{} nice strings".format(n_nice))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
