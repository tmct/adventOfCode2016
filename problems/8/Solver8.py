import re

def rotate_list(steps, values):
    return values[-steps:] + values[:-steps]


class Solver8:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.pixels = [[False for i in range(self.grid_height)] for j in range(self.grid_width)]

    def get_number_lit_pixels(self, instruction_file_name, debug=False):
        with open(instruction_file_name, 'r') as instruction_file:
            for line in instruction_file:
                if debug:
                    self.print_grid()
                self.perform_instruction(line.strip())
        self.print_grid()
        return len([pixel for col in self.pixels for pixel in col if pixel])

    def print_grid(self):
        for col in self.pixels:
            line = ''
            for pixel in col:
                if pixel:
                    line += '#'
                else:
                    line += '.'
            print(line)
        print('')

    def perform_instruction(self, instruction_string):
        if instruction_string.startswith('rect'):
            rect_width, rect_height = map(int, instruction_string[5:].split('x'))
            self.set_top_left_pixels(rect_width, rect_height)
            return
        if instruction_string.startswith('rotate'):
            rotate_instruction = instruction_string[7:]
            rotate_row = False
            if rotate_instruction.startswith('column'):
                rotate_detail = rotate_instruction[7:]
            else:
                rotate_row = True
                rotate_detail = rotate_instruction[4:]
            match = re.search('(\d*) by (\d*)', rotate_detail)
            index = int(match.group(1))
            rot_number = int(match.group(2))
            self.perform_rotation(index, rot_number, rotate_row)

    def set_top_left_pixels(self, rect_width, rect_height):
        for i in range(rect_height):
            for j in range(rect_width):
                self.pixels[i][j] = True

    def perform_rotation(self, index, rot_number, rotate_row):
        if rotate_row:
            row_to_rotate = self.pixels[index]
            self.pixels[index] = rotate_list(rot_number, row_to_rotate)
        else:
            column_to_rotate = [self.pixels[i][index] for i in range(self.grid_width)]
            rotated_column = rotate_list(rot_number, column_to_rotate)
            for i, value in enumerate(rotated_column):
                self.pixels[i][index] = value

