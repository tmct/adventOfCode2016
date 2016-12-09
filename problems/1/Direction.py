from enum import Enum


class Direction(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

    def turn(self, turn):
        new_direction = (self.value + turn.value) % 4
        return Direction(new_direction)

    @classmethod
    def get_i_component(cls, dir):
        if dir == cls.east:
            return 1
        if dir == cls.west:
            return -1
        return 0

    @classmethod
    def get_j_component(cls, dir):
        if dir == cls.north:
            return 1
        if dir == cls.south:
            return -1
        return 0

