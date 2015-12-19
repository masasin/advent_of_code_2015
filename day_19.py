"""
adventofcode.com/day/19

--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly,
and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is
going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry
isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission
plant, capable of constructing any Red-Nosed Reindeer molecule you need. It
works by starting with some input molecule and then doing a series of
replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration
involves determining the number of molecules that can be generated in one step
from a given starting point.

For example, imagine a simpler machine that supports only the following
replacements:

    - H => HO
    - H => OH
    - O => HH

Given the replacements above and starting with HOH, the following molecules
could be generated:

    - HOOH (via H => HO on the first H).
    - HOHO (via H => HO on the second H).
    - OHOH (via H => OH on the first H).
    - HOOH (via H => OH on the second H).
    - HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH
appears twice) after one replacement from HOH. Santa's favorite molecule,
HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and
three from O).

The machine replaces without regard for the surrounding characters. For example,
given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom,
the medicine molecule for which you need to calibrate the machine. How many
distinct molecules can be created after all the different ways you can do one
replacement on the medicine molecule?

--- Part Two ---

Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e, and applying
replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

    - e => H
    - e => O
    - H => HO
    - H => OH
    - O => HH

If you'd like to make HOH, you start with e, and then make the following
replacements:

    - e => O to get O
    - O => HH to get HH
    - H => OH (on the second H) to get HOH

So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be
made in 6 steps.

How long will it take to make the medicine? Given the available replacements and
the medicine molecule in your puzzle input, what is the fewest number of steps
to go from e to the medicine molecule?

"""
from collections import defaultdict
import re


def parse(stream):
    replacements = defaultdict(list)
    for k, v in re.findall(r"(\w+) => (\w+)", stream):
        replacements[k].append(v)
    return replacements, stream.strip().split("\n")[-1]


def reverse_dict(d):
    reverse = defaultdict(list)
    for k, v in d.items():
        for i in v:
            reverse[i].append(k)
    return reverse


def generate_next(starter, replacements):
    molecules = set()

    for i, char in enumerate(starter):
        try:
            if char in replacements:
                for replacement in replacements[char]:
                    molecules.add(starter[:i] + replacement + starter[i + 1:])
            else:
                for replacement in replacements[starter[i:i + 2]]:
                    molecules.add(starter[:i] + replacement + starter[i + 2:])
        except KeyError:
            continue

    return molecules


def generate_prev(target, replacements):
    molecules = set()

    for key, sources in replacements.items():
        idx = target.find(key)
        while idx >= 0:
            for elem in sources:
                if elem == "e":
                    continue
                try:
                    molecules.add(target[:idx] + elem + target[idx + len(key):])
                except IndexError:
                    molecules.add(target[:idx] + elem)
            idx = target.find(key, idx + 1)

    if not molecules:
        molecules = {"e"}
    return molecules


def count_molecules(starter, replacements):
    return len(generate_next(starter, replacements))


def steps_to_generate(target, replacements):
    replacements = reverse_dict(replacements)
    seen = {}
    last_generation = generate_prev(target, replacements)
    n_steps = 1

    while last_generation != {"e"}:
        current_generation = set()
        molecule = min(last_generation, key=len)

        try:
            new_molecules = seen[molecule]
        except KeyError:
            new_molecules = generate_prev(molecule, replacements)
            seen[molecule] = new_molecules
        current_generation |= new_molecules
        last_generation = current_generation

        n_steps += 1

    return n_steps


def part_one():
    with open("inputs/day_19_input.txt") as fin:
        replacements, starter = parse(fin.read())
    print(count_molecules(starter, replacements))


def part_two():
    with open("inputs/day_19_input.txt") as fin:
        replacements, target = parse(fin.read())
    print(steps_to_generate(target, replacements))


if __name__ == '__main__':
    part_one()
    part_two()
