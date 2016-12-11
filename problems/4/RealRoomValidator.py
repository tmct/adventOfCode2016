from Room import Room


class RealRoomValidator:
    def get_real_rooms_sector_id_sum(self, room_file):
        valid_sector_id_sum = 0
        for line in room_file:
            room_name = line[:-1]
            room = Room(room_name)
            if room.is_valid():
                valid_sector_id_sum += room.sector_id
        return valid_sector_id_sum
