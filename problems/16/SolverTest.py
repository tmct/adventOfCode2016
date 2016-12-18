import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_something(self):
        output = Solver().solve(20, '10000')
        self.assertEqual('01100', output)

    def test_real(self):
        output = Solver().solve(272, '10001001100000001')
        self.assertEqual('10101001010100001', output)

    def test_real_big(self):
        output = Solver().solve(35651584, '10001001100000001')
        self.assertEqual('10100001110101001', output)


if __name__ == '__main__':
    unittest.main()
