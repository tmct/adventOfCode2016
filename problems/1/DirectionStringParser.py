from Turn import Turn


class DirectionStringParser:
    @classmethod
    def parse(cls, direction_string):
        instruction_list = map(str.strip, direction_string.split(','))
        turns = []
        leaps = []
        for instruction in instruction_list:
            turn, leap = cls.parse_instruction(instruction)
            turns.append(turn)
            leaps.append(leap)
        return turns, leaps

    @classmethod
    def parse_instruction(cls, instruction):
        turn_char = instruction[0]
        leap_string = instruction[1:]
        turn = cls.parse_turn_char(turn_char)
        leap = cls.parse_leap_string(leap_string)
        return turn, leap

    @classmethod
    def parse_turn_char(cls, turn_char):
        if turn_char == 'R':
            return Turn.right
        if turn_char == 'L':
            return Turn.left
        raise ValueError

    @classmethod
    def parse_leap_string(cls, leap_string):
        return int(leap_string)