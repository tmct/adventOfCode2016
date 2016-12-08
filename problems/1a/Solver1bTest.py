import unittest
from Solver1b import Solver1b


class Solver1aTest(unittest.TestCase):
    def test_example(self):
        solver = Solver1b()
        shortest_path = solver.get_distance_to_first_repeat_visit("R8, R4, R4, R8")
        self.assertEqual(shortest_path, 4)

    def test_bad_example(self):
        solver = Solver1b()
        with self.assertRaises(Exception) as context:
            shortest_path = solver.get_distance_to_first_repeat_visit("R4, R4, R8, R8")
        self.assertTrue('No location visited twice' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
