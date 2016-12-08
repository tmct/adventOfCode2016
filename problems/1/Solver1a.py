from DirectionStringParser import DirectionStringParser
from Position import Position


class Solver1a:
    def get_shortest_path(self, directions_string):
        turns, leaps = DirectionStringParser.parse(directions_string)
        position = Position()
        for turn, leap in zip(turns, leaps):
            position.turn(turn)
            position.walk_forward(leap)
        return abs(position.x_coord) + abs(position.y_coord)
