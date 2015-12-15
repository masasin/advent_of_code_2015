from collections import namedtuple

from day_14 import parse, Reindeer, Race


Parameters = namedtuple("Parameters", ["d_fly", "t_fly", "t_rest"])


def test_parse():
    line_1 = ("Comet can fly 14 km/s for 10 seconds, but then must rest for 127"
              "seconds.")
    line_2 = ("Dancer can fly 16 km/s for 11 seconds, but then must rest for"
              "162 seconds.")
    assert parse(line_1) == ("Comet", 14, 10, 127)
    assert parse(line_2) == ("Dancer", 16, 11, 162)


class TestReindeer(object):
    def setup(self):
        self.name = "Comet"
        self.params = Parameters(14, 10, 127)
        self.reindeer = Reindeer(self.name, *self.params)

    def test_init(self):
        assert self.reindeer.name == self.name
        assert self.reindeer.d_fly == self.params.d_fly
        assert self.reindeer.t_fly == self.params.t_fly
        assert self.reindeer.t_rest == self.params.t_rest
        assert self.reindeer.points == 0
        assert self.reindeer.time == 0
        assert self.reindeer.position == 0
        assert self.reindeer.state == "flying"
        assert self.reindeer.state_change_time == self.params.t_fly

    def test_step_once(self):
        self.reindeer.step()
        assert self.reindeer.time == 1
        assert self.reindeer.position == self.params.d_fly
        assert self.reindeer.state == "flying"
        assert self.reindeer.state_change_time == self.params.t_fly

    def test_step_until_state_change(self):
        self.reindeer.step(self.params.t_fly)
        assert self.reindeer.time == self.params.t_fly
        assert self.reindeer.position == self.params.t_fly * self.params.d_fly
        assert self.reindeer.state == "resting"
        assert self.reindeer.state_change_time == (self.params.t_fly +
                                                   self.params.t_rest)

    def test_step_until_next_state_change(self):
        self.reindeer.step(self.params.t_fly + self.params.t_rest)
        assert self.reindeer.time == self.params.t_fly + self.params.t_rest
        assert self.reindeer.position == self.params.t_fly * self.params.d_fly
        assert self.reindeer.state == "flying"
        assert self.reindeer.state_change_time == (2*self.params.t_fly +
                                                   self.params.t_rest)


class TestRace(object):
    def setup(self):
        self.race = Race()
        self.race.add(Reindeer("Comet", 14, 10, 127))
        self.race.add(Reindeer("Dancer", 16, 11, 162))

    def test_t_1(self):
        self.race.step()
        assert self.race.reindeer["Comet"].position == 14
        assert self.race.reindeer["Comet"].state == "flying"
        assert self.race.reindeer["Comet"].points == 0

        assert self.race.reindeer["Dancer"].position == 16
        assert self.race.reindeer["Dancer"].state == "flying"
        assert self.race.reindeer["Dancer"].points == 1

    def test_t_10(self):
        self.race.step(10)
        assert self.race.reindeer["Comet"].position == 140
        assert self.race.reindeer["Comet"].state == "resting"

        assert self.race.reindeer["Dancer"].position == 160
        assert self.race.reindeer["Dancer"].state == "flying"

    def test_t_11(self):
        self.race.step(11)
        assert self.race.reindeer["Comet"].position == 140
        assert self.race.reindeer["Comet"].state == "resting"

        assert self.race.reindeer["Dancer"].position == 176
        assert self.race.reindeer["Dancer"].state == "resting"

    def test_t_138(self):
        self.race.step(138)
        assert self.race.reindeer["Comet"].position == 154
        assert self.race.reindeer["Comet"].state == "flying"

        assert self.race.reindeer["Dancer"].position == 176
        assert self.race.reindeer["Dancer"].state == "resting"

    def test_t_140(self):
        self.race.step(140)
        assert self.race.reindeer["Comet"].points == 1
        assert self.race.reindeer["Dancer"].points == 139

    def test_t_174(self):
        self.race.step(174)
        assert self.race.reindeer["Comet"].position == 280
        assert self.race.reindeer["Comet"].state == "resting"

        assert self.race.reindeer["Dancer"].position == 192
        assert self.race.reindeer["Dancer"].state == "flying"

    def test_t_1000(self):
        self.race.step(1000)
        assert self.race.reindeer["Comet"].position == 1120
        assert self.race.reindeer["Comet"].state == "resting"
        assert self.race.reindeer["Comet"].points == 312

        assert self.race.reindeer["Dancer"].position == 1056
        assert self.race.reindeer["Dancer"].state == "resting"
        assert self.race.reindeer["Dancer"].points == 689

    def test_max_position(self):
        self.race.step(1)
        assert self.race.max_position() == 16
        self.race.step(999)
        assert self.race.max_position() == 1120

    def test_max_points(self):
        self.race.step(1)
        assert self.race.max_points() == 1
        self.race.step(999)
        assert self.race.max_points() == 689
