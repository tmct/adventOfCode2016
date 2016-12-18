import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_example_1(self):
        output = Solver('ihgpwlah').solve()
        self.assertEqual('DDRRRD', output)

    def test_example_2(self):
        output = Solver('kglvqrro').solve()
        self.assertEqual('DDUDRLRRUDRD', output)

    def test_example_3(self):
        output = Solver('ulqzkmiv').solve()
        self.assertEqual('DRURDRUDDLLDLUURRDULRLDUUDDDRR', output)

    def test_real(self):
        output = Solver('rrrbmfta').solve()
        self.assertEqual('RLRDRDUDDR', output)

    def test_example_1_longest(self):
        output = Solver('ihgpwlah').solve_longest()
        self.assertEqual(370, output)

    def test_example_2_longest(self):
        output = Solver('kglvqrro').solve_longest()
        self.assertEqual(492, output)

    def test_example_3_longest(self):
        output = Solver('ulqzkmiv').solve_longest()
        self.assertEqual(830, output)

    def test_real_longest(self):
        output = Solver('rrrbmfta').solve_longest()
        self.assertEqual(420, output)


if __name__ == '__main__':
    unittest.main()
