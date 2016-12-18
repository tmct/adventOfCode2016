import re

ABCD = 'abcd'
copy_regex = r'cpy (\S+) (\S+)'
inc_regex = r'inc ([abcd])'
dec_regex = r'dec ([abcd])'
jump_regex = r'jnz (\S+) (-?\d+)'


class Solver:
    def __init__(self):
        self.registers = [0, 0, 0, 0]
        self.instructions = None
        self.current_instruction_index = 0
        self.number_of_instructions = None

    def get_a_register_value(self, input_file_name):
        self.parse_instructions(input_file_name)
        # then run function starting with first instruction
        self.run_program()
        return self.registers[0]

    def get_a_register_value_with_c_bodge(self, input_file_name):
        self.registers[2] = 1
        return self.get_a_register_value(input_file_name)

    def parse_instructions(self, input_file_name):
        instructions = []
        with open(input_file_name, 'r') as input_file:
            for line in input_file:
                instruction = self.get_instruction_method(line.strip())
                instructions.append(instruction)
        self.instructions = tuple(instructions)
        self.number_of_instructions = len(self.instructions)

    def get_instruction_method(self, instruction_string):
        m = re.search(copy_regex, instruction_string)
        if m:
            origin = m.group(1)
            destination = ABCD.index(m.group(2))
            if origin in ABCD:
                register = ABCD.index(origin)

                def copy_from_register_to_register():
                    self.registers[destination] = self.registers[register]
                    self.current_instruction_index += 1

                return copy_from_register_to_register
            else:
                value = int(origin)

                def copy_int_value_to_register():
                    self.registers[destination] = value
                    self.current_instruction_index += 1

                return copy_int_value_to_register
        m = re.search(inc_regex, instruction_string)
        if m:
            value = int(ABCD.index(m.group(1)))

            def increment_register():
                self.registers[value] += 1
                self.current_instruction_index += 1

            return increment_register
        m = re.search(dec_regex, instruction_string)
        if m:
            value = int(ABCD.index(m.group(1)))

            def decrement_register():
                self.registers[value] -= 1
                self.current_instruction_index += 1

            return decrement_register
        m = re.search(jump_regex, instruction_string)
        if m:
            check_value = m.group(1)
            jump_size = int(m.group(2))
            if check_value in ABCD:
                register = ABCD.index(check_value)

                def jump():
                    _jump_size = int(jump_size)
                    if not self.registers[register]:
                        _jump_size = 1
                    self.current_instruction_index += _jump_size
                return jump

            else:
                value = int(check_value)

                if not value:
                    jump_size = 1

                def jump():
                    self.current_instruction_index += jump_size

                return jump
        raise Exception('Line not parsed as a known instruction: {}'.format(instruction_string))

    def run_program(self):
        counter = 0
        while self.current_instruction_index < self.number_of_instructions:
            next_instruction = self.instructions[self.current_instruction_index]
            next_instruction()
            counter += 1
        print('Program terminated after {} instructions'.format(counter))
