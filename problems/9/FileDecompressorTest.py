import unittest
from FileDecompressor import FileDecompressor


class FileDecompressorTest(unittest.TestCase):
    def test_sample_data(self):
        output = FileDecompressor().get_decompressed_length('test_input.txt')
        self.assertEqual(57, output)

    def test_proper_data(self):
        output = FileDecompressor().get_decompressed_length('input.txt')
        self.assertEqual(107035, output)

    def test_sample_data_b(self):
        output = FileDecompressor().get_decompressed_length_v2('test_input_b.txt')
        self.assertEqual(242394, output)

    def test_proper_data_b(self):
        output = FileDecompressor().get_decompressed_length_v2('input.txt')
        self.assertEqual(11451628995, output)


if __name__ == '__main__':
    unittest.main()
