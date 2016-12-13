from Decompressor import Decompressor


class FileDecompressor:
    def get_decompressed_length(self, input_file_name):
        decompressor = Decompressor()
        with open(input_file_name, 'r') as input_file:
            return sum(decompressor.get_decompressed_length(line.strip()) for line in input_file)
