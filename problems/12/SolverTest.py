import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_example(self):
        output = Solver().get_a_register_value('test_input.txt')
        self.assertEqual(42, output)

    def test_real(self):
        output = Solver().get_a_register_value('input.txt')
        self.assertEqual(318020, output)

    def test_real_b(self):
        output = Solver().get_a_register_value_with_c_bodge('input.txt')
        self.assertEqual(9227674, output)


if __name__ == '__main__':
    unittest.main()
