import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_something(self):
        output = Solver().solve('input')
        self.assertEqual(1, output)


if __name__ == '__main__':
    unittest.main()
