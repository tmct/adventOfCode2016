from Direction import Direction


class InstructionsParser():
    def parse_instructions_string(self, instructions_string):
        return [self.get_move_list(line) for line in instructions_string.splitlines()]

    def get_move_list(self, line):
        return [Direction.from_symbol(char) for char in line]
