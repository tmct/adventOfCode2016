from hashlib import md5
from collections import deque

# up down left right
x_comps = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
y_comps = {'U': -1, 'D': 1, 'L': 0, 'R': 0}


def get_destination(path):
    x = sum(x_comps[char] for char in path)
    y = sum(y_comps[char] for char in path)
    return x, y


def get_silly_directions(destination):
    silly = []
    x, y = destination
    if x == 0:
        silly.append('L')
    if x == 3:
        silly.append('R')
    if y == 0:
        silly.append('U')
    if y == 3:
        silly.append('D')
    return silly


class Solver:
    def __init__(self, initial_code):
        self.initial_code = initial_code

    def solve(self):
        initial_room = (0, 0)
        desired_room = (3, 3)
        discovered_paths = deque()
        discovered_paths.append('')
        while discovered_paths:
            path = discovered_paths.popleft()
            destination = get_destination(path)
            allowed_directions_by_hash = self.allowed_directions(path)
            silly_directions = get_silly_directions(destination)
            for direction in allowed_directions_by_hash:
                if direction in silly_directions:
                    continue
                new_path = path + direction
                if get_destination(new_path) == (3, 3):
                    return new_path
                discovered_paths.append(new_path)

    def solve_longest(self):
        initial_room = (0, 0)
        desired_room = (3, 3)
        discovered_paths = deque()
        discovered_paths.append('')
        longest = 0
        while discovered_paths:
            path = discovered_paths.pop()
            destination = get_destination(path)
            allowed_directions_by_hash = self.allowed_directions(path)
            silly_directions = get_silly_directions(destination)
            for direction in allowed_directions_by_hash:
                if direction in silly_directions:
                    continue
                new_path = path + direction
                if get_destination(new_path) == (3, 3):
                    longest = max(longest, len(new_path))
                else:
                    discovered_paths.append(new_path)
        return longest

    def allowed_directions(self, path):
        directions = 'UDLR'
        allowed_directions = [char in 'bcdef' for char in self.hash_string(path)[:4]]
        return [direction for direction, allowed in zip(directions, allowed_directions) if allowed]

    def hash_string(self, string):
        hash_input_string = self.initial_code + string
        hash_input = hash_input_string.encode()
        return md5(hash_input).hexdigest()
