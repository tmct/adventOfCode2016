from Direction import Direction


class Position:
    def __init__(self, direction=Direction.north):
        self.x_coord = 0
        self.y_coord = 0
        self.direction = direction

    def turn(self, turn):
        self.direction = self.direction.turn(turn)