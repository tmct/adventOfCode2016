import unittest
from .Solver1a import Solver1a


class Solver1aTest(unittest.TestCase):
    def test_upper(self):
        solver = Solver1a()
        shortest_path = solver.get_shortest_path("R2, L3")
        self.assertEqual(shortest_path, 5)


if __name__ == '__main__':
    unittest.main()
