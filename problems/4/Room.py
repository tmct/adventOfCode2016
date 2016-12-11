from collections import defaultdict


class Room:
    def __init__(self, room_name):
        name_and_id, checksum_fragment = room_name.split('[')
        self.checksum = checksum_fragment[:-1]
        name_and_id_split = name_and_id.split('-')
        self.sector_id = int(name_and_id_split[-1])
        self.name = ''.join(name_and_id_split[:-1])
        self.full_name = '-'.join(name_and_id_split[:-1])

    def is_valid(self):
        letter_frequencies = defaultdict(int)
        for letter in self.name:
            letter_frequencies[letter] += 1
        top_letters_by_frequency = sorted(letter_frequencies, key=lambda letter: -letter_frequencies[letter] + 0.01*ord(letter))
        putative_checksum = ''.join(top_letters_by_frequency[:5])
        return self.checksum == putative_checksum

    def get_decrypted_name(self):
        decrypted_name = ''
        shift = self.sector_id % 26
        for character in self.full_name:
            if character == '-':
                decrypted_name += ' '
                continue
            old_char_index = ord(character)
            new_char_index = old_char_index + shift
            if new_char_index > ord('z'):
                new_char_index -= 26
            decrypted_name += chr(new_char_index)
        return decrypted_name