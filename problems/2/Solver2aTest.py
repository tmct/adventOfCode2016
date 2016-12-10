import unittest
from .Solver2a import Solver2a


class Solver2aTest(unittest.TestCase):
    def test_example(self):
        solver = Solver2a()
        # noinspection SpellCheckingInspection
        shortest_path = solver.get_bathroom_code(
            'ULL\n'
            'RRDDD\n'
            'LURDL\n'
            'UUUUD\n')
        self.assertEqual(shortest_path, '1985')


if __name__ == '__main__':
    unittest.main()
