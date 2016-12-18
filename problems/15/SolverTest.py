import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_something_example(self):
        primes = (5, 2)
        remainders = (0, 1)
        output = Solver().solve(primes, remainders)
        self.assertEqual(5, output)

    def test_something(self):
        primes = (3, 5, 7, 13, 17, 19)
        remainders = (2, 4, 0, 7, 1, 12)
        output = Solver().solve(primes, remainders)
        self.assertEqual(400589, output)


if __name__ == '__main__':
    unittest.main()
