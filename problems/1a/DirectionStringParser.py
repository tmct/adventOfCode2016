from Turn import Turn


class DirectionStringParser:
    # noinspection PyPep8Naming
    @staticmethod
    def parse(directionString):
        turns = [Turn.left, Turn.right]
        leaps = [2, 3]
        return turns, leaps

    # def get_directions(self):
    #     list(map(self.parse_thing(map(str.strip, self.directions_string.split(','))))
    #
    # @staticmethod
    # def parse_thing(intermediate):
    #     return [intermediate[0] == 'L',int(intermediate[1:])]