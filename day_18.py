"""
http://adventofcode.com/day/18

--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at
most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal
lighting configuration. With so few lights, he says, you'll have to resort to
animation.

Start by setting your lights to the included initial configuration (your puzzle
input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration
based on the current one. Each light's next state (either on or off) depends on
its current state and the current states of the eight lights adjacent to it
(including diagonals). Lights on the edge of the grid might have fewer than
eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors
numbered 1 through 8, and the light marked B, which is on an edge, only has the
neighbors marked 1 through 5:

    1B5...
    234...
    ......
    ..123.
    ..8A4.
    ..765.

The state a light should have next is based on its current state (on or off)
plus the number of neighbors that are on:

    - A light which is on stays on when 2 or 3 neighbors are on, and turns off
      otherwise.
    - A light which is off turns on if exactly 3 neighbors are on, and stays off
      otherwise.

All of the lights update simultaneously; they all consider the same current
state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

    Initial state:
    .#.#.#
    ...##.
    #....#
    ..#...
    #.#..#
    ####..

    After 1 step:
    ..##..
    ..##.#
    ...##.
    ......
    #.....
    #.##..

    After 2 steps:
    ..###.
    ......
    ..###.
    ......
    .#....
    .#....

    After 3 steps:
    ...#..
    ......
    ...#..
    ..##..
    ......
    ......

    After 4 steps:
    ......
    ......
    ..##..
    ..##..
    ......
    ......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many
lights are on after 100 steps?

--- Part Two ---

You flip the instructions over; Santa goes on to point out that this is all just
an implementation of Conway's Game of Life. At least, it was, until you notice
that something's wrong with the grid of lights you bought: four lights, one in
each corner, are stuck on and can't be turned off. The example above will
actually run like this:

    Initial state:
    ##.#.#
    ...##.
    #....#
    ..#...
    #.#..#
    ####.#

    After 1 step:
    #.##.#
    ####.#
    ...##.
    ......
    #...#.
    #.####

    After 2 steps:
    #..#.#
    #....#
    .#.##.
    ...##.
    .#..##
    ##.###

    After 3 steps:
    #...##
    ####.#
    ..##.#
    ......
    ##....
    ####.#

    After 4 steps:
    #.####
    #....#
    ...#..
    .##...
    #.....
    #.#..#

    After 5 steps:
    ##.###
    .##..#
    .##...
    .##...
    #.#...
    ##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the
four corners always in the on state, how many lights are on after 100 steps?

"""
import numpy as np


class Game(object):
    def __init__(self, inital_state, broken=False):
        self.state = self.parse(inital_state)
        self.shape = self.state.shape
        self.broken = broken
        self._set_broken_lights()

    def _set_broken_lights(self):
        if self.broken:
            x, y = self.shape
            self.state[0, 0] = 1
            self.state[0, y-1] = 1
            self.state[x-1, 0] = 1
            self.state[x-1, y-1] = 1

    @staticmethod
    def parse(initial_state):
        config = []
        for line in initial_state.strip().split("\n"):
            config.append([0 if i == "." else 1 for i in line])
        return np.array(config)

    def get_n_neighbours(self, x, y):
        total = -self.state[x, y]
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if 0 <= x + dx < self.shape[0] and 0 <= y + dy < self.shape[1]:
                    total += self.state[x + dx, y + dy]
        return total

    def get_next_state(self, x, y):
        if (self.broken and x in (0, self.shape[0]-1) and
                y in (0, self.shape[1]-1)):
            return 1
        if not self.state[x, y] and self.get_n_neighbours(x, y) == 3:
            return 1
        elif self.state[x, y] and self.get_n_neighbours(x, y) not in (2, 3):
            return 0
        else:
            return self.state[x, y]

    def step(self, n_steps=1):
        for i in range(n_steps):
            next_state = self.state.copy()
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    next_state[x, y] = self.get_next_state(x, y)
            self.state = next_state

    @property
    def n_lights_on(self):
        return np.sum(self.state)


def part_one():
    with open("inputs/day_18_input.txt") as fin:
        game = Game(fin.read())
    game.step(100)
    print("{} lights on".format(game.n_lights_on))


def part_two():
    with open("inputs/day_18_input.txt") as fin:
        game = Game(fin.read(), broken=True)
    game.step(100)
    print("{} lights on".format(game.n_lights_on))


if __name__ == '__main__':
    part_one()
    part_two()
