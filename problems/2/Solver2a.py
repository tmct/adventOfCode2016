from InstructionsParser import InstructionsParser
from Position import Position


class Solver2a:
    def get_bathroom_code(self, instructions_string):
        instructions = InstructionsParser().parse_instructions_string(instructions_string)
        position = Position()
        code = ''
        for move_list in instructions:
            for direction in move_list:
                position.move_in_direction(direction)
            code += position.get_digit()
        return code
