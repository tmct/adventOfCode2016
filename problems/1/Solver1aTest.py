import unittest
from Solver1a import Solver1a


class Solver1aTest(unittest.TestCase):
    def test_example_1(self):
        solver = Solver1a()
        shortest_path = solver.get_shortest_path("R2, L3")
        self.assertEqual(shortest_path, 5)

    def test_example_2(self):
        solver = Solver1a()
        shortest_path = solver.get_shortest_path("R2, R2, R2")
        self.assertEqual(shortest_path, 2)

    def test_example_3(self):
        solver = Solver1a()
        shortest_path = solver.get_shortest_path("R5, L5, R5, R3")
        self.assertEqual(shortest_path, 12)


if __name__ == '__main__':
    unittest.main()
