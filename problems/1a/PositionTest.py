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

    def test_turn_left_from_west(self):
        position = Position(direction=Direction.west)

        position.turn(Turn.left)

        self.assertEqual(position.x_coord, 0)
        self.assertEqual(position.y_coord, 0)
        self.assertEqual(position.direction, Direction.south)

    def test_turn_right_from_west(self):
        position = Position(direction=Direction.west)

        position.turn(Turn.right)

        self.assertEqual(position.x_coord, 0)
        self.assertEqual(position.y_coord, 0)
        self.assertEqual(position.direction, Direction.north)

    def test_go_forwards_3(self):
        position = Position()

        position.walk_forward(3)

        self.assertEqual(position.x_coord, 0)
        self.assertEqual(position.y_coord, 3)
        self.assertEqual(position.direction, Direction.north)

    def test_go_forwards_2_from_south(self):
        position = Position(Direction.south)

        position.walk_forward(2)

        self.assertEqual(position.x_coord, 0)
        self.assertEqual(position.y_coord, -2)
        self.assertEqual(position.direction, Direction.south)

    def test_go_forwards_4_from_east(self):
        position = Position(Direction.east)

        position.walk_forward(4)

        self.assertEqual(position.x_coord, 4)
        self.assertEqual(position.y_coord, 0)
        self.assertEqual(position.direction, Direction.east)
