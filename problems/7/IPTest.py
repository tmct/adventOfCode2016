import unittest
from IP import IP


# noinspection SpellCheckingInspection
class IPTest(unittest.TestCase):
    def test_example_1(self):
        ip = IP('abba[mnop]qrst')
        self.assertTrue(ip.supports_tls)

    def test_example_2(self):
        ip = IP('abcd[bddb]xyyx')
        self.assertFalse(ip.supports_tls)

    def test_example_3(self):
        ip = IP('aaaa[qwer]tyui')
        self.assertFalse(ip.supports_tls)

    def test_example_4(self):
        ip = IP('ioxxoj[asdfgh]zxcvbn')
        self.assertTrue(ip.supports_tls)

if __name__ == '__main__':
    unittest.main()
