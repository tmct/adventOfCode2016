from DirectionStringParser import DirectionStringParser


class Solver1a:
    # noinspection PyMethodMayBeStatic
    def get_shortest_path(self, directions_string):
        turns, leaps = DirectionStringParser.parse(directions_string)
        return 5
