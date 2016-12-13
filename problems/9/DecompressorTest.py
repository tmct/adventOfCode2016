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

    def test_example_1b(self):
        output = Decompressor().get_decompressed_length_v2('(3x3)XYZ')
        self.assertEqual(9, output)

    def test_example_2b(self):
        output = Decompressor().get_decompressed_length_v2('X(8x2)(3x3)ABCY')
        self.assertEqual(20, output)

    def test_example_2c(self):
        output = Decompressor().get_decompressed_length_v2('(27x12)(20x12)(13x14)(7x10)(1x12)A')
        self.assertEqual(241920, output)

    def test_example_2d(self):
        output = Decompressor().get_decompressed_length_v2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')
        self.assertEqual(445, output)

if __name__ == '__main__':
    unittest.main()
