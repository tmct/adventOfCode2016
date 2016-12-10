import unittest
from .Solver2b import Solver2b


class Solver2bTest(unittest.TestCase):
    def test_example(self):
        solver = Solver2b()
        # noinspection SpellCheckingInspection
        code = solver.get_bathroom_code(
            'ULL\n'
            'RRDDD\n'
            'LURDL\n'
            'UUUUD\n')
        self.assertEqual(code, '5DB3')

    def test_my_example(self):
        solver = Solver2b()
        # noinspection SpellCheckingInspection
        code = solver.get_bathroom_code(
            'UDDU\n'
            'RDDRDLL\n'
            'URUR\n')
        self.assertEqual(code, '5D9')


if __name__ == '__main__':
    unittest.main()
