from hashlib import md5
from collections import deque

import re

run_of_three_regex = r'(.)\1\1'
run_of_five_regex = r'(.)\1\1\1\1'


def get_run_of_five_chars(digest):
    match = re.search(run_of_five_regex, digest)
    if not match:
        return set()
    return set(match.groups())


def get_first_triply_repeated_char(digest):
    match = re.search(run_of_three_regex, digest)
    if not match:
        return None
    return match.group(1)


class Solver:
    def __init__(self, salt):
        self.salt = salt
        self.five_matches = deque()
        self.current_index = 0
        self.keys = []

    def solve(self):
        for i in range(1, 1001):
            digest = self.get_hash_digest(i)
            runs_of_five_chars = get_run_of_five_chars(digest)
            self.five_matches.append(runs_of_five_chars)
        while len(self.keys) < 64:
            digest = self.get_hash_digest(self.current_index)
            triply_repeated_character = get_first_triply_repeated_char(digest)
            if triply_repeated_character:
                if triply_repeated_character in {char for matches in self.five_matches for char in matches}:
                    self.keys.append(triply_repeated_character)
            self.update_five_matches()
            self.current_index += 1
        return self.current_index - 1

    def solve_with_stretching(self):
        for i in range(self.current_index + 1, self.current_index + 1001):
            digest = self.get_hash_digest_with_stretching(i)
            runs_of_five_chars = get_run_of_five_chars(digest)
            self.five_matches.append(runs_of_five_chars)
        while len(self.keys) < 64:
            digest = self.get_hash_digest_with_stretching(self.current_index)
            triply_repeated_character = get_first_triply_repeated_char(digest)
            if triply_repeated_character:
                if triply_repeated_character in {char for matches in self.five_matches for char in matches}:
                    self.keys.append(triply_repeated_character)
            self.update_five_matches_with_stretching()
            self.current_index += 1
        return self.current_index - 1

    def get_hash_digest(self, counter):
        hash_input_string = self.salt + str(counter)
        hash_input = hash_input_string.encode()
        return md5(hash_input).hexdigest()

    def get_hash_digest_with_stretching(self, counter):
        hash_input_string = self.salt + str(counter)
        hash_input = hash_input_string.encode()
        hash_output = md5(hash_input).hexdigest()
        for i in range(2016):
            hash_input = hash_output.encode()
            hash_output = md5(hash_input).hexdigest()
        return hash_output

    def update_five_matches(self):
        self.five_matches.popleft()
        digest = self.get_hash_digest(self.current_index + 1001)
        runs_of_five_chars = get_run_of_five_chars(digest)
        self.five_matches.append(runs_of_five_chars)

    def update_five_matches_with_stretching(self):
        self.five_matches.popleft()
        digest = self.get_hash_digest_with_stretching(self.current_index + 1001)
        runs_of_five_chars = get_run_of_five_chars(digest)
        self.five_matches.append(runs_of_five_chars)
