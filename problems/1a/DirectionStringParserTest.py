import unittest

from Turn import Turn
from DirectionStringParser import DirectionStringParser


class DirectionStringParserTest(unittest.TestCase):

    def test_example_1(self):
        turns, leaps = DirectionStringParser.parse("R2, L3")
        self.assertEqual(turns, [Turn.right, Turn.left])
        self.assertEqual(leaps, [2, 3])

    def test_example_2(self):
        turns, leaps = DirectionStringParser.parse("R2, R2, R2")
        self.assertEqual(turns, [Turn.right, Turn.right, Turn.right])
        self.assertEqual(leaps, [2, 2, 2])

    def test_example_3(self):
        turns, leaps = DirectionStringParser.parse("R5, L5, R5, R3")
        self.assertEqual(turns, [Turn.right, Turn.left, Turn.right, Turn.right])
        self.assertEqual(leaps, [5, 5, 5, 3])
