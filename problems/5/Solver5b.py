import hashlib
import sys
import random
import string

lowercase_hex_digits = string.hexdigits[:-6]


def is_valid_position(position_char):
    return position_char in [str(i) for i in range(8)]


class Solver5b:
    def __init__(self):
        self.password_digits = [None for i in range(8)]
        self.hacker_style = False

    def find_password(self, door_id, hacker_style=False):
        self.hacker_style = hacker_style
        counter = 0
        while self.need_more_digits():
            if hacker_style and not counter % 10000:
                self.print_hacker_output()
            hash_digest = self.get_hash_digest(counter, door_id)
            if hash_digest[:5] == '00000':
                position_char = hash_digest[5]
                if not is_valid_position(position_char):
                    counter += 1
                    continue
                position = int(position_char)
                if self.position_not_filled(position):
                    self.set_password_digit(position, hash_digest[6])
            counter += 1
        if hacker_style:
            self.print_hacker_output(final=True)
        return ''.join(self.password_digits)

    def print_hacker_output(self, final=False):
        hacker_string = "\rDECRYPTING PASSWORD: "
        if final:
            hacker_string = "\rPASSWORD  DECRYPTED: "
        for i in range(8):
            dec_digit = self.password_digits[i]
            if not dec_digit:
                dec_digit = random.choice(lowercase_hex_digits)
            hacker_string += dec_digit
        if final:
            hacker_string += '\n'

        sys.stdout.write(hacker_string)
        sys.stdout.flush()

    def get_hash_digest(self, counter, door_id):
        hash_input_string = door_id + str(counter)
        hash_input = hash_input_string.encode()
        return hashlib.md5(hash_input).hexdigest()

    def position_not_filled(self, position):
        return not bool(self.password_digits[position])

    def set_password_digit(self, position, digit):
        self.password_digits[position] = digit

    def need_more_digits(self):
        return None in self.password_digits
