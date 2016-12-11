import hashlib


class Solver5a:
    def find_password(self, door_id):
        counter = 0
        password_digits = ''
        while len(password_digits) < 8:
            hash_digest = self.get_hash_digest(counter, door_id)
            if hash_digest[:5] == '00000':
                password_digits += hash_digest[5]
            counter += 1
        return password_digits

    def get_hash_digest(self, counter, door_id):
        hash_input_string = door_id + str(counter)
        hash_input = hash_input_string.encode()
        return hashlib.md5(hash_input).hexdigest()