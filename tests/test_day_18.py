import pytest
import numpy as np

from day_18 import Game


initial_state = (".#.#.#\n"
                 "...##.\n"
                 "#....#\n"
                 "..#...\n"
                 "#.#..#\n"
                 "####..")


def test_parse():
    assert np.all(Game.parse(initial_state) ==
                  np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 1, 0, 1, 0],
                            [0, 0, 0, 0, 1, 1, 0, 0],
                            [0, 1, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 1, 0, 1, 0, 0, 1, 0],
                            [0, 1, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
                           ))


class TestGame(object):
    def setup(self):
        self.game = Game(initial_state)

    def test_initialize(self):
        assert np.all(self.game.state == np.array([[0, 1, 0, 1, 0, 1],
                                                   [0, 0, 0, 1, 1, 0],
                                                   [1, 0, 0, 0, 0, 1],
                                                   [0, 0, 1, 0, 0, 0],
                                                   [1, 0, 1, 0, 0, 1],
                                                   [1, 1, 1, 1, 0, 0]]))
        assert self.game.shape == (6, 6)

    def test_get_n_neighbours(self):
        assert np.all(self.game.get_n_neighbours() ==
                      np.array([[1, 0, 3, 2, 4, 1],
                                [2, 2, 3, 2, 4, 3],
                                [0, 2, 2, 3, 3, 1],
                                [2, 4, 1, 2, 2, 2],
                                [2, 6, 4, 4, 2, 0],
                                [2, 4, 3, 2, 2, 1]]))

    def test_step_once(self):
        self.game.step()
        assert np.all(self.game.state == np.array([[0, 0, 1, 1, 0, 0],
                                                   [0, 0, 1, 1, 0, 1],
                                                   [0, 0, 0, 1, 1, 0],
                                                   [0, 0, 0, 0, 0, 0],
                                                   [1, 0, 0, 0, 0, 0],
                                                   [1, 0, 1, 1, 0, 0]]))

    def test_step_n_times(self):
        self.game.step(4)
        assert np.all(self.game.state == np.array([[0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0],
                                                   [0, 0, 1, 1, 0, 0],
                                                   [0, 0, 1, 1, 0, 0],
                                                   [0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0]]))

    def test_n_lights_on(self):
        assert self.game.n_lights_on == 15
        self.game.step(4)
        assert self.game.n_lights_on == 4


class TestBrokenGame(object):
    def setup(self):
        self.game = Game(initial_state, broken=True)

    def test_initialize(self):
        assert np.all(self.game.state == np.array([[1, 1, 0, 1, 0, 1],
                                                   [0, 0, 0, 1, 1, 0],
                                                   [1, 0, 0, 0, 0, 1],
                                                   [0, 0, 1, 0, 0, 0],
                                                   [1, 0, 1, 0, 0, 1],
                                                   [1, 1, 1, 1, 0, 1]]))
        assert self.game.shape == (6, 6)

    def test_get_n_neighbours(self):
        print(self.game.get_n_neighbours())
        assert np.all(self.game.get_n_neighbours() ==
                      np.array([[1, 1, 3, 2, 4, 1],
                                [3, 3, 3, 2, 4, 3],
                                [0, 2, 2, 3, 3, 1],
                                [2, 4, 1, 2, 2, 2],
                                [2, 6, 4, 4, 3, 1],
                                [2, 4, 3, 2, 3, 1]]))

    def test_step_once(self):
        self.game.step()
        assert np.all(self.game.state == np.array([[1, 0, 1, 1, 0, 1],
                                                   [1, 1, 1, 1, 0, 1],
                                                   [0, 0, 0, 1, 1, 0],
                                                   [0, 0, 0, 0, 0, 0],
                                                   [1, 0, 0, 0, 1, 0],
                                                   [1, 0, 1, 1, 1, 1]]))

    def test_step_n_times(self):
        self.game.step(5)
        assert np.all(self.game.state == np.array([[1, 1, 0, 1, 1, 1],
                                                   [0, 1, 1, 0, 0, 1],
                                                   [0, 1, 1, 0, 0, 0],
                                                   [0, 1, 1, 0, 0, 0],
                                                   [1, 0, 1, 0, 0, 0],
                                                   [1, 1, 0, 0, 0, 1]]))

    def test_n_lights_on(self):
        assert self.game.n_lights_on == 17
        self.game.step(5)
        assert self.game.n_lights_on == 17
