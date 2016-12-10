import unittest
from VerticalTriangleFileValidator import VerticalTriangleFileValidator


class Solver2bTest(unittest.TestCase):
    def test_example(self):
        with open('test_input.txt', 'r') as input_file:
            number_valid_triangles = VerticalTriangleFileValidator().get_number_of_valid_triangles(input_file)
            self.assertEqual(number_valid_triangles, 3)


if __name__ == '__main__':
    unittest.main()
