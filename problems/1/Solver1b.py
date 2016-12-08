from DirectionStringParser import DirectionStringParser
from Position import Position


class Solver1b:
    def get_distance_to_first_repeat_visit(self, directions_string):
        turns, leaps = DirectionStringParser.parse(directions_string)
        position = Position()
        locations_visited = {position.location()}
        for turn, leap in zip(turns, leaps):
            position.turn(turn)
            for _ in range(leap):
                position.walk_forward(1)
                location = position.location()
                if location in locations_visited:
                    return abs(position.x_coord) + abs(position.y_coord)
                else:
                    locations_visited.add(location)
        raise Exception("No location visited twice")
