import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_something(self):
        output = Solver().solve('test_input.txt')
        self.assertEqual(3, output)

    def test_real(self):
        output = Solver().solve('input.txt')
        self.assertEqual(0, output)

    def test_something_b(self):
        output = Solver().solve_b('test_input.txt', 10)
        self.assertEqual(2, output)

    def test_real_b(self):
        output = Solver().solve_b('input.txt', 2**32)
        self.assertEqual(109, output)


if __name__ == '__main__':
    unittest.main()
