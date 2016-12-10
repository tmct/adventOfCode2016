from enum import Enum


class Direction(Enum):
    up = 0
    right = 1
    down = 2
    left = 3

    @classmethod
    def from_symbol(cls, symbol):
        symbol_map = {
            'U': 0,
            'D': 2,
            'L': 3,
            'R': 1
        }
        return cls(symbol_map[symbol])

    def get_i_component(self):
        if self == Direction.left:
            return 1
        if self == Direction.right:
            return -1
        return 0

    def get_j_component(self):
        if self == Direction.up:
            return 1
        if self == Direction.down:
            return -1
        return 0

