import unittest

class Solver5aTest(unittest.TestCase):
    def test_example(self):
        password = Solver5a.find_password('abc')
        self.assertEqual(password, '18f47a30')

if __name__ == '__main__':
    unittest.main()