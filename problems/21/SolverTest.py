import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def testmove_example(self):
        output = Solver('abcde').solve('test_input.txt')
        self.assertEqual('decab', output)

    def test_real(self):
        output = Solver('abcdefgh').solve('input.txt')
        self.assertEqual('hcdefbag', output)

    def test_example_reverse(self):
        output = Solver('hcdefbag', decrypt=True).solve('input.txt')
        self.assertEqual('abcdefgh', output)

    def test_example_reverse_real(self):
        output = Solver('fbgdceah', decrypt=True).solve('input.txt')
        self.assertEqual('fbhaegdc', output)


if __name__ == '__main__':
    unittest.main()
