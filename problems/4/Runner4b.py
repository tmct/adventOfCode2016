from RealRoomValidator import RealRoomValidator


def main():
    with open('input.txt', 'r') as room_file:
        RealRoomValidator().find_north_pole_storage(room_file)


if __name__ == '__main__':
    main()
