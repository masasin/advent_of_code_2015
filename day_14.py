"""
http://adventofcode.com/day/14

--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must
rest occasionally to recover their energy. Santa would like to know which of his
reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not
moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

- Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
- Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten
seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh
second, Comet begins resting (staying at 140 km), and Dancer continues on for a
total distance of 176 km. On the 12th second, both reindeer are resting. They
continue to rest until the 138th second, when Comet flies for another ten
seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet
is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point).
So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly
2503 seconds, what distance has the winning reindeer traveled?

--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old
scoring system.

Instead, at the end of each second, he awards one point to the reindeer
currently in the lead. (If there are multiple reindeer tied for the lead, they
each get one point.) He keeps the traditional 2503 second time limit, of course,
as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the
lead and gets one point. He stays in the lead until several seconds into Comet's
second burst: after the 140th second, Comet pulls into the lead and gets his
first point. Of course, since Dancer had been in the lead for the 139 seconds
before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet,
our old champion, only has 312. So, with the new scoring system, Dancer would
win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after
exactly 2503 seconds, how many points does the winning reindeer have?

"""
import re


def parse(line):
    space = line.index(" ")
    name = line[:space]
    d_fly, t_fly, t_rest = [int(i) for i in re.findall(r"(\d+)", line[space:])]
    return name, d_fly, t_fly, t_rest


class Reindeer(object):
    def __init__(self, name, d_fly, t_fly, t_rest):
        self.name = name
        self.d_fly = d_fly
        self.t_fly = t_fly
        self.t_rest = t_rest

        self.points = 0
        self.time = 0
        self.position = 0
        self.state = "flying"
        self.state_change_time = t_fly

    def step(self, n_steps=1):
        for i in range(n_steps):
            self.time += 1
            if self.state == "flying":
                self.position += self.d_fly
            if self.time == self.state_change_time:
                if self.state == "flying":
                    self.state = "resting"
                    self.state_change_time += self.t_rest
                else:
                    self.state = "flying"
                    self.state_change_time += self.t_fly

    def __repr__(self):
        return "{} at {} km".format(self.name, self.position)


class Race(object):
    def __init__(self):
        self.reindeer = {}

    def add(self, deer):
        self.reindeer[deer.name] = deer

    def step(self, n_steps=1):
        for step in range(n_steps):
            for deer in self.reindeer.values():
                deer.step()
            max_distance = self.max_position()
            for deer in self.reindeer.values():
                if deer.position == max_distance:
                    deer.points += 1

    def max_position(self):
        return max(v.position for v in self.reindeer.values())

    def max_points(self):
        return max(v.points for v in self.reindeer.values())


def part_one():
    race = Race()
    with open("inputs/day_14_input.txt") as fin:
        for line in fin.readlines():
            race.add(Reindeer(*parse(line)))
    race.step(2503)
    print("Winning distance: {} km".format(race.max_position()))


def part_two():
    race = Race()
    with open("inputs/day_14_input.txt") as fin:
        for line in fin.readlines():
            race.add(Reindeer(*parse(line)))
    race.step(2503)
    print("Winning score: {} points".format(race.max_points()))


if __name__ == "__main__":
    part_one()
    part_two()
