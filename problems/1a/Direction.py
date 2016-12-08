from enum import Enum


class Direction(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

    def turn(self, turn):
        new_direction = (self.value + turn.value) % 4
        return Direction(new_direction)



