import unittest
from Decompressor import Decompressor


class DecompressorTest(unittest.TestCase):
    def test_example_1(self):
        output = Decompressor().get_decompressed_length('ADVENT')
        self.assertEqual(6, output)

    def test_example_2(self):
        output = Decompressor().get_decompressed_length('A(1x5)BC')
        self.assertEqual(7, output)

    def test_example_3(self):
        output = Decompressor().get_decompressed_length('(3x3)XYZ')
        self.assertEqual(9, output)

    def test_example_4(self):
        output = Decompressor().get_decompressed_length('A(2x2)BCD(2x2)EFG')
        self.assertEqual(11, output)

    def test_example_5(self):
        output = Decompressor().get_decompressed_length('(6x1)(1x3)A')
        self.assertEqual(6, output)

    def test_example_6(self):
        output = Decompressor().get_decompressed_length('X(8x2)(3x3)ABCY')
        self.assertEqual(18, output)


if __name__ == '__main__':
    unittest.main()
