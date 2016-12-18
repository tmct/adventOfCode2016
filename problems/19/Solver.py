from itertools import islice


def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


class Solver:
    def __init__(self):
        self.tile_is_safe = None
        self.last_row = None
        self.total_safe = None

    def number_of_safe_tiles(self, first_row, total_rows):
        width = len(first_row)
        self.last_row = [char == '.' for char in first_row]
        self.total_safe = sum(self.last_row)
        for i in range(1, total_rows):
            self.add_row()
        return self.total_safe

    def add_row(self):
        new_row = []
        extended_last_row = [True] + self.last_row + [True]
        for a, b, c in window(extended_last_row, 3):
            new_row.append(a == c)
        self.total_safe += sum(new_row)
        self.last_row = new_row
