class Position(object):
    def __init__(self):
        self.x = 1
        self.y = 1

    def get_digit(self):
        index = (2 - self.x) + 3 * (2 - self.y)
        return str(index + 1)

    def move_in_direction(self, direction):
        i_move = direction.get_i_component()
        j_move = direction.get_j_component()
        new_i_coordinate = self.x + i_move
        new_j_coordinate = self.y + j_move
        if 0 <= new_i_coordinate < 3:
            self.x = new_i_coordinate
        if 0 <= new_j_coordinate < 3:
            self.y = new_j_coordinate