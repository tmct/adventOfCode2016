import unittest
from Solver5a import Solver5a
from Solver5b import Solver5b


class Solver5Test(unittest.TestCase):
    def test_example_a(self):
        password = Solver5a().find_password('abc')
        self.assertEqual('18f47a30', password)

    def test_real_input_a(self):
        password = Solver5a().find_password('cxdnnyjw')
        self.assertEqual('f77a0e6e', password)

    def test_example_b(self):
        password = Solver5b().find_password('abc')
        self.assertEqual('05ace8e3', password)

    def test_real_input_b(self):
        password = Solver5b().find_password('cxdnnyjw')
        self.assertEqual('999828ec', password)


if __name__ == '__main__':
    unittest.main()
