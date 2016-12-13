import re


class Decompressor:
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
