from enum import Enum


class Direction(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

    def turn(self, turn):
        new_direction = (self.value + turn.value) % 4
        return Direction(new_direction)

    def get_i_component(self):
        if self == self.east:
            return 1
        if self == self.west:
            return -1
        return 0

    def get_j_component(self):
        if self == self.north:
            return 1
        if self == self.south:
            return -1
        return 0

