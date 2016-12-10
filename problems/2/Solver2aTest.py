import unittest
from .Solver2a import Solver2a


class Solver2aTest(unittest.TestCase):
    def test_example(self):
        solver = Solver2a()
        # noinspection SpellCheckingInspection
        code = solver.get_bathroom_code(
            'ULL\n'
            'RRDDD\n'
            'LURDL\n'
            'UUUUD\n')
        self.assertEqual(code, '1985')

    def test_my_example(self):
        solver = Solver2a()
        # noinspection SpellCheckingInspection
        code = solver.get_bathroom_code(
            'UDDU\n'
            'RDDRDLL\n'
            'URUR\n')
        self.assertEqual(code, '573')


if __name__ == '__main__':
    unittest.main()
