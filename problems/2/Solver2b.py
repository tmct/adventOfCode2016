from InstructionsParser import InstructionsParser
from Direction import Direction


class Solver2b:
    def get_bathroom_code(self, instructions_string):
        instructions = InstructionsParser().parse_instructions_string(instructions_string)
        position = '5'
        code = ''
        for move_list in instructions:
            for direction in move_list:
                position = direction_matrix[position][direction]
            code += position
        return code

direction_matrix = {
    '1': {
        Direction.up: '1',
        Direction.right: '1',
        Direction.down: '3',
        Direction.left: '1',
    },
    '2': {
        Direction.up: '2',
        Direction.right: '3',
        Direction.down: '6',
        Direction.left: '2',
    },
    '3': {
        Direction.up: '1',
        Direction.right: '4',
        Direction.down: '7',
        Direction.left: '2',
    },
    '4': {
        Direction.up: '4',
        Direction.right: '4',
        Direction.down: '8',
        Direction.left: '3',
    },
    '5': {
        Direction.up: '5',
        Direction.right: '6',
        Direction.down: '5',
        Direction.left: '5',
    },
    '6': {
        Direction.up: '2',
        Direction.right: '7',
        Direction.down: 'A',
        Direction.left: '5',
    },
    '7': {
        Direction.up: '3',
        Direction.right: '8',
        Direction.down: 'B',
        Direction.left: '6',
    },
    '8': {
        Direction.up: '4',
        Direction.right: '9',
        Direction.down: 'C',
        Direction.left: '7',
    },
    '9': {
        Direction.up: '9',
        Direction.right: '9',
        Direction.down: '9',
        Direction.left: '8',
    },
    'A': {
        Direction.up: '6',
        Direction.right: 'B',
        Direction.down: 'A',
        Direction.left: 'A',
    },
    'B': {
        Direction.up: '7',
        Direction.right: 'C',
        Direction.down: 'D',
        Direction.left: 'A',
    },
    'C': {
        Direction.up: '8',
        Direction.right: 'C',
        Direction.down: 'C',
        Direction.left: 'B',
    },
    'D': {
        Direction.up: 'B',
        Direction.right: 'D',
        Direction.down: 'D',
        Direction.left: 'D',
    },
}
