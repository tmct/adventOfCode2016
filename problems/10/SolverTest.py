import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_sample(self):
        compare_bot_index = Solver().find_compare_bot('test_input.txt', 2, 5)
        self.assertEqual(2, compare_bot_index)

    def test_real(self):
        compare_bot_index = Solver().find_compare_bot('input.txt', 61, 17)
        self.assertEqual(93, compare_bot_index)

    def test_output_product(self):
        product = Solver().get_first_three_outputs_product('input.txt')
        self.assertEqual(47101, product)


if __name__ == '__main__':
    unittest.main()
