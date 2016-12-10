import unittest
from RealRoomValidator import RealRoomValidator


class Solver4aTest(unittest.TestCase):
    def test_example(self):
        with open('test_input.txt', 'r') as room_file:
            sector_id_sum = RealRoomValidator().get_real_rooms_sector_id_sum(room_file)
            self.assertEqual(sector_id_sum, 1514)


if __name__ == '__main__':
    unittest.main()
