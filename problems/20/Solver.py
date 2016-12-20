class Solver:
    def __init__(self):
        self.starts_to_highest_ends = {}
        self.index_of_start = None
        self.current_start = None
        self.sorted_starts = None
        self.total = None

    def solve(self, input_file_name):
        starts_to_highest_ends = {}
        with open(input_file_name) as input_file:
            for line in input_file:
                start, end = map(int, line.strip().split('-'))
                if start not in starts_to_highest_ends or end > starts_to_highest_ends[start]:
                    starts_to_highest_ends[start] = end
        current_ip = 0
        new_ip = starts_to_highest_ends[current_ip] + 1

        while current_ip < new_ip:
            current_ip += 1
            if current_ip not in starts_to_highest_ends:
                continue
            end = starts_to_highest_ends[current_ip]
            if end > new_ip:
                new_ip = end + 1
        return current_ip

    def solve_b(self, input_file_name, total):
        self.total = total
        number_valid = total

        with open(input_file_name) as input_file:
            for line in input_file:
                start, end = map(int, line.strip().split('-'))
                if end <= start:
                    raise Exception('bad data!')
                if start not in self.starts_to_highest_ends or end > self.starts_to_highest_ends[start]:
                    self.starts_to_highest_ends[start] = end

        self.sorted_starts = sorted(self.starts_to_highest_ends)

        self.index_of_start = 0
        while self.index_of_start != len(self.sorted_starts):
            self.current_start = self.sorted_starts[self.index_of_start]
            range_start = self.current_start
            range_end = self.find_next_valid_ip_after() - 1
            print(range_start, range_end)
            number_valid -= (range_end - range_start + 1)
        return number_valid

    def find_next_valid_ip_after(self):
        start_of_range = self.current_start
        current_end_of_range = self.starts_to_highest_ends[start_of_range]
        while True:
            self.index_of_start += 1
            if self.index_of_start == len(self.sorted_starts):
                return current_end_of_range + 1
            new_start = self.sorted_starts[self.index_of_start]
            if new_start > current_end_of_range:
                return current_end_of_range + 1
            potential_end_of_range = self.starts_to_highest_ends[new_start]
            if potential_end_of_range > current_end_of_range:
                current_end_of_range = potential_end_of_range




