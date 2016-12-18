import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_example(self):
        output = Solver('abc').solve()
        self.assertEqual(22728, output)

    def test_real(self):
        output = Solver('jlmsuwbz').solve()
        self.assertEqual(35186, output)

    def test_example_2016(self):
        output = Solver('abc').solve_with_stretching()
        self.assertEqual(22551, output)

    def test_real_2016(self):
        output = Solver('jlmsuwbz').solve_with_stretching()
        self.assertEqual(22429, output)


if __name__ == '__main__':
    unittest.main()
