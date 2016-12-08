import unittest

from Direction import Direction
from Position import Position
from Turn import Turn


class PositionTest(unittest.TestCase):

    def test_initial_position(self):
        position = Position()
        self.assertEqual(position.x_coord, 0)
        self.assertEqual(position.y_coord, 0)
        self.assertEqual(position.direction, Direction.north)

    def test_turn_right(self):
        position = Position()
        position.turn(Turn.right)
        self.assertEqual(position.x_coord, 0)
        self.assertEqual(position.y_coord, 0)
        self.assertEqual(position.direction, Direction.east)
