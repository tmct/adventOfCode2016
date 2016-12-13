import unittest
from FileDecompressor import FileDecompressor


class FileDecompressorTest(unittest.TestCase):
    def test_sample_data(self):
        output = FileDecompressor().get_decompressed_length('test_input.txt')
        self.assertEqual(57, output)

    def test_proper_data(self):
        output = FileDecompressor().get_decompressed_length('input.txt')
        self.assertEqual(107035, output)


if __name__ == '__main__':
    unittest.main()
