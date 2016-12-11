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

    def test_example_1_b(self):
        ip = IP('aba[bab]xyz')
        self.assertTrue(ip.supports_ssl)

    def test_example_2_b(self):
        ip = IP('xyx[xyx]xyxz')
        self.assertFalse(ip.supports_ssl)

    def test_example_3_b(self):
        ip = IP('aaa[kek]eke')
        self.assertTrue(ip.supports_ssl)

    def test_example_4_b(self):
        ip = IP('zazbz[bzb]cdb')
        self.assertTrue(ip.supports_ssl)

if __name__ == '__main__':
    unittest.main()
