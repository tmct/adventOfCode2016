import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_circle_1(self):
        output = Solver().solve(1)
        self.assertEqual(1, output)

    def test_circle_2(self):
        output = Solver().solve(2)
        self.assertEqual(1, output)

    def test_circle_3(self):
        output = Solver().solve(3)
        self.assertEqual(3, output)

    def test_circle_4(self):
        output = Solver().solve(4)
        self.assertEqual(1, output)

    def test_circle_5(self):
        output = Solver().solve(5)
        self.assertEqual(3, output)

    def test_circle_6(self):
        output = Solver().solve(6)
        self.assertEqual(5, output)

    def test_circle_7(self):
        output = Solver().solve(7)
        self.assertEqual(7, output)

    def test_circle_8(self):
        output = Solver().solve(8)
        self.assertEqual(1, output)

    def test_circle_11(self):
        output = Solver().solve(11)
        self.assertEqual(7, output)

    def test_circle_input(self):
        output = Solver().solve(3001330)
        self.assertEqual(1808357, output)

    def test_circle_5_b(self):
        output = Solver().solve_b(5)
        self.assertEqual(2, output)

    def test_circle_8_b(self):
        output = Solver().solve_b(8)
        self.assertEqual(7, output)

    def test_circle_11_b(self):
        output = Solver().solve_b(11)
        self.assertEqual(2, output)

    def test_circle_input_b(self):
        output = Solver().solve_b(3001330)
        self.assertEqual(1407007, output)


if __name__ == '__main__':
    unittest.main()
