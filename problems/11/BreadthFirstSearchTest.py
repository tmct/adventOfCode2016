import unittest
import BreadthFirstSearch
from State import State
import cProfile


class BreadthFirstTest(unittest.TestCase):
    def test_example(self):
        start_state = State(0, (0, 0), (1, 2))
        target_state = State(3, (3, 3), (3, 3))
        output = BreadthFirstSearch.BreadthFirstSearch().find_distance(start_state, target_state)
        self.assertEqual(11, output)

    def test_real(self):
        start_state = State(0, (0, 0, 2, 1, 1), (0, 0, 1, 1, 1))
        target_state = State(3, (3, 3, 3, 3, 3), (3, 3, 3, 3, 3))
        output = BreadthFirstSearch.BreadthFirstSearch().find_distance(start_state, target_state)
        self.assertEqual(37, output)

    def test_profile(self):
        start_state = State(0, (0, 0, 0, 0, 2, 1, 1), (0, 0, 0, 0, 1, 1, 1))
        target_state = State(3, (3, 3, 3, 3, 3, 3, 3), (3, 3, 3, 3, 3, 3, 3))
        cProfile.runctx('BreadthFirstSearch.BreadthFirstSearch(30000).find_distance(start_state, target_state)', globals(), locals())

    def test_real_b(self):
        start_state = State(0, (0, 0, 0, 0, 2, 1, 1), (0, 0, 0, 0, 1, 1, 1))
        target_state = State(3, (3, 3, 3, 3, 3, 3, 3), (3, 3, 3, 3, 3, 3, 3))
        output = BreadthFirstSearch.BreadthFirstSearch().find_distance(start_state, target_state)
        self.assertEqual(61, output)


if __name__ == '__main__':
    unittest.main()
