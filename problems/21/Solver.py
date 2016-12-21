import re

swap_positions_regex = r'swap position (\d+) with position (\d+)'
swap_letters_regex = r'swap letter (.) with letter (.)'
rotate_regex = r'rotate (left|right) (\d+)'
rotate_on_letter_position_regex = r'rotate based on position of letter (.)'
reverse_slice_regex = r'reverse positions (\d+) through (\d+)'
move_regex = r'move position (\d+) to position (\d+)'


class Solver:
    def __init__(self, start_string, decrypt = False):
        self.buffer = list(start_string)
        self.instructions = []
        self.decrypt = decrypt
        self.reverse_shift = {int(i): int(j) for i, j in zip('13572460', '76542107')}

    def solve(self, input_file_name):
        intermediates = [''.join(self.buffer)]
        with open(input_file_name, 'r') as input_file:
            for line in input_file:
                self.add_instruction(line.strip())
        if self.decrypt:
            self.instructions = self.instructions[::-1]
        for instruction in self.instructions:
            instruction()
        #    intermediates.append(''.join(self.buffer))
        # if not self.decrypt:
        #     intermediates = intermediates[::-1]
        # for i in intermediates:
        #     print(i)
        return ''.join(self.buffer)

    def add_instruction(self, instruction_string):
        match = re.search(swap_positions_regex, instruction_string)
        if match:
            return self.add_swap_positions_instruction(match)
        match = re.search(swap_letters_regex, instruction_string)
        if match:
            return self.add_swap_letters_instruction(match)
        match = re.search(rotate_regex, instruction_string)
        if match:
            return self.add_rotate_instruction(match)
        match = re.search(rotate_on_letter_position_regex, instruction_string)
        if match:
            return self.add_rotate_on_letter_position_instruction(match)
        match = re.search(reverse_slice_regex, instruction_string)
        if match:
            return self.reverse_slice_instruction(match)
        match = re.search(move_regex, instruction_string)
        if match:
            return self.move_instruction(match)
        raise Exception('Could not parse line! "{}"'.format(instruction_string))

    def add_swap_positions_instruction(self, match):
        first, second = (int(group) for group in match.groups())

        def swap_positions():
            self.buffer[first], self.buffer[second] = self.buffer[second], self.buffer[first]

        self.instructions.append(swap_positions)

    def add_swap_letters_instruction(self, match):
        def swap_letters():
            first, second = (self.buffer.index(group) for group in match.groups())
            self.buffer[first], self.buffer[second] = self.buffer[second], self.buffer[first]

        self.instructions.append(swap_letters)

    def add_rotate_instruction(self, match):
        steps = int(match.group(2)) % len(self.buffer)
        if match.group(1) == 'left':
            steps = (len(self.buffer) - steps) % len(self.buffer)
        if self.decrypt:
            steps = (len(self.buffer) - steps) % len(self.buffer)

        def rotate():
            self.buffer = self.buffer[-steps:] + self.buffer[:-steps]

        self.instructions.append(rotate)

    def add_rotate_on_letter_position_instruction(self, match):

        def rotate_on_letter_position():
            if self.decrypt:
                final_index = self.buffer.index(match.group(1)) % 8
                steps = self.reverse_shift[final_index]
            else:
                steps = 1 + self.buffer.index(match.group(1))
                if steps >= 5:
                    steps += 1
                steps %= len(self.buffer)
            self.buffer = self.buffer[-steps:] + self.buffer[:-steps]

        self.instructions.append(rotate_on_letter_position)

    def reverse_slice_instruction(self, match):
        first, second = (int(group) for group in match.groups())

        def reverse_slice():
            self.buffer = self.buffer[:first] + self.buffer[first:second + 1][::-1] + self.buffer[second + 1:]
        self.instructions.append(reverse_slice)

    def move_instruction(self, match):
        first, second = (int(group) for group in match.groups())
        if self.decrypt:
            first, second = second, first

        def move():
            value = self.buffer[first]
            del self.buffer[first]
            self.buffer.insert(second, value)
        self.instructions.append(move)
