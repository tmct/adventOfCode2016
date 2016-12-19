class Solver:
    def __init__(self):
        self.adjacent_elves = {}

    def solve(self, start_number):
        recipient = 1
        remaining = start_number
        power = 1
        while remaining > 1:
            new_remaining = remaining // 2
            remaining_was_odd = remaining % 2
            power *= 2
            remaining = new_remaining
            if remaining_was_odd:
                recipient += power
        return recipient

    def solve_b(self, start_number):
        self.adjacent_elves = {index: (index - 1, index + 1) for index in range(start_number)}
        self.adjacent_elves[0] = (start_number - 1, 1)
        self.adjacent_elves[start_number - 1] = (start_number - 2, 0)

        first_elf_to_delete = start_number // 2
        current_elf = first_elf_to_delete
        elves_remaining = start_number
        while elves_remaining > 1:
            elf_to_delete = current_elf
            current_elf = self.adjacent_elves[current_elf][1]
            if elves_remaining % 2:
                current_elf = self.adjacent_elves[current_elf][1]
            self.delete_elf(elf_to_delete)
            elves_remaining -= 1

        return current_elf + 1

    def delete_elf(self, target_elf):
        before, after = self.adjacent_elves[target_elf]
        two_before = self.adjacent_elves[before][0]
        self.adjacent_elves[before] = (two_before, after)
        two_after = self.adjacent_elves[after][1]
        self.adjacent_elves[after] = (before, two_after)
