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
    def __init__(self, initial_state, broken=False):
        self._state = self.parse(initial_state)
        shape = self.state.shape
        self.x_max = shape[0] - 1
        self.y_max = shape[1] - 1
        self.broken = broken
        self._set_broken_lights()

    def _set_broken_lights(self):
        if self.broken:
            self.state[0, 0] = 1
            self.state[0, self.y_max] = 1
            self.state[self.x_max, 0] = 1
            self.state[self.x_max, self.y_max] = 1

    @property
    def state(self):
        return self._state[1:-1, 1:-1]

    @state.setter
    def state(self, new_state):
        self._state[1:-1, 1:-1] = new_state

    @staticmethod
    def parse(initial_state):
        size_x = initial_state.index("\n")
        size_y = initial_state.strip().count("\n") + 1
        state = np.zeros((size_x + 2, size_y + 2), dtype=np.uint8)
        for i, line in enumerate(initial_state.strip().split("\n")):
            for j, char in enumerate(line):
                state[i + 1, j + 1] = 0 if char == "." else 1
        return state

    def get_n_neighbours(self):
        return (self._state[0:-2, 0:-2] + self._state[0:-2, 1:-1] +
                self._state[0:-2, 2:] + self._state[1:-1, 0:-2] +
                self._state[1:-1, 2:] + self._state[2:, 0:-2] +
                self._state[2:, 1:-1] + self._state[2:, 2:])

    def step(self, n_steps=1):
        for i in range(n_steps):
            n_neighbours = self.get_n_neighbours()

            birth = (n_neighbours == 3) & (self._state[1:-1, 1:-1] == 0)
            survive = (((n_neighbours == 2) | (n_neighbours == 3)) &
                       (self._state[1:-1, 1:-1] == 1))

            self._state[...] = 0
            self._state[1:-1, 1:-1][birth | survive] = 1
            self._set_broken_lights()

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
