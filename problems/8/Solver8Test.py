import unittest
from Solver8 import Solver8


class Solver8Test(unittest.TestCase):
    def test_count_test_ips(self):
        instruction_file_name = 'test_input.txt'
        number_of_lit_pixels = Solver8(3, 7).get_number_lit_pixels(instruction_file_name)
        self.assertEqual(6, number_of_lit_pixels)

    def test_count_test_ips_real(self):
        instruction_file_name = 'input.txt'
        number_of_lit_pixels = Solver8(6, 50).get_number_lit_pixels(instruction_file_name)
        self.assertEqual(121, number_of_lit_pixels)

if __name__ == '__main__':
    unittest.main()