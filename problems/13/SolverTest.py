import unittest
from Maze import Maze


class SolverTest(unittest.TestCase):
    def test_example(self):
        output = Maze(10).get_shortest_path((1, 1), (7, 4))
        self.assertEqual(11, output)

    def test_real(self):
        output = Maze(1358).get_shortest_path((1, 1), (31, 39))
        self.assertEqual(96, output)

    def test_example_b_1(self):
        output = Maze(10).find_nodes_n_away((1, 1), 0)
        self.assertEqual(1, output)

    def test_example_b_2(self):
        output = Maze(10).find_nodes_n_away((1, 1), 1)
        self.assertEqual(3, output)

    def test_example_b_3(self):
        output = Maze(10).find_nodes_n_away((1, 1), 2)
        self.assertEqual(5, output)

    def test_example_b_4(self):
        output = Maze(10).find_nodes_n_away((1, 1), 3)
        self.assertEqual(6, output)

    def test_real_b(self):
        output = Maze(1358).find_nodes_n_away((1, 1), 50)
        self.assertEqual(141, output)


if __name__ == '__main__':
    unittest.main()
