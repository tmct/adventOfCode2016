import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_example_1(self):
        output = Solver().number_of_safe_tiles('..^^.', 3)
        self.assertEqual(6, output)

    def test_example_2(self):
        output = Solver().number_of_safe_tiles('.^^.^.^^^^', 10)
        self.assertEqual(38, output)

    def test_real(self):
        output = Solver().number_of_safe_tiles(
            '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.', 40)
        self.assertEqual(1956, output)

    def test_real_long(self):
        output = Solver().number_of_safe_tiles(
            '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.',
            400000)
        self.assertEqual(19995121, output)


if __name__ == '__main__':
    unittest.main()
