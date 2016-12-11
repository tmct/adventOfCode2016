import unittest
from Room import Room


class RoomTest(unittest.TestCase):
    def test_example(self):
        r = Room('qzmt-zixmtkozy-ivhz-343[whatever]')
        dec_name = r.get_decrypted_name()
        self.assertEqual(dec_name, 'very encrypted name')


if __name__ == '__main__':
    unittest.main()
