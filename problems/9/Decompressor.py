import re


class Decompressor:
    def __init__(self):
        self.repeat_counts = []
        self.compressed_string = ''

    def get_decompressed_length(self, compressed_string):
        string_left_to_decompress = compressed_string
        decompressed_string = ''
        repeat_marker = r'\((\d+)x(\d+)\)'
        while True:
            match = re.search(repeat_marker, string_left_to_decompress)
            if not match:
                break
            num_repeat_chars = int(match.group(1))
            repeat_count = int(match.group(2))
            repeat_chars = string_left_to_decompress[match.end():match.end() + num_repeat_chars]
            expanded_repeat = repeat_count * repeat_chars
            decompressed_string += string_left_to_decompress[:match.start()] + expanded_repeat
            string_left_to_decompress = string_left_to_decompress[match.end() + num_repeat_chars:]
        decompressed_string += string_left_to_decompress
        return len(decompressed_string)

    def get_decompressed_length_v2(self, compressed_string):
        self.repeat_counts = [1 for i in compressed_string]
        self.compressed_string = compressed_string

        self.set_multipliers(0, len(self.compressed_string), 1)
        return sum(self.repeat_counts)

    def set_multipliers(self, start_index, end_index, multiplier):
        sub_start_index = start_index
        for i in range(start_index, end_index):
            self.repeat_counts[i] *= multiplier

        string_left_to_decompress = self.compressed_string[start_index:end_index]

        repeat_marker = r'\((\d+)x(\d+)\)'
        while True:
            match = re.search(repeat_marker, string_left_to_decompress)
            if not match:
                break
            num_repeat_chars = int(match.group(1))
            repeat_count = int(match.group(2))

            for i in range(sub_start_index + match.start(), sub_start_index + match.end()):
                self.repeat_counts[i] = 0

            self.set_multipliers(sub_start_index + match.end(), sub_start_index + match.end() + num_repeat_chars, repeat_count)
            string_left_to_decompress = string_left_to_decompress[match.end() + num_repeat_chars:]
            sub_start_index += match.end() + num_repeat_chars