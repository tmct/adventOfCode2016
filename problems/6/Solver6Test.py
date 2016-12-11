import unittest
from Solver6 import Solver6


class Solver6Test(unittest.TestCase):
    def test_example_input_a(self):
        input_file = 'test_input.txt'
        solver = Solver6(input_file)
        message = solver.get_message()
        self.assertEqual('easter', message)

    def test_real_input_a(self):
        input_file = 'input.txt'
        solver = Solver6(input_file)
        message = solver.get_message()
        self.assertEqual('umcvzsmw', message)

    def test_example_input_b(self):
        input_file = 'test_input.txt'
        solver = Solver6(input_file)
        message = solver.get_message_using_modified_code()
        self.assertEqual('advent', message)

    def test_real_input_b(self):
        input_file = 'input.txt'
        solver = Solver6(input_file)
        message = solver.get_message_using_modified_code()
        self.assertEqual('rwqoacfz', message)

if __name__ == '__main__':
    unittest.main()
