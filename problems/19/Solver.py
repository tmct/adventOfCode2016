class Solver:
    def __init__(self):
        self.next_elves = {}

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
        self.next_elves = {index: index + 1 for index in range(start_number)}
        self.next_elves[start_number - 1] = 0
        current_elf_index = 0
        elves_remaining = start_number
        while elves_remaining > 1:
            target_elf = current_elf_index
            jump_distance = elves_remaining // 2
            for i in range(jump_distance):
                previous_elf = target_elf
                target_elf = self.next_elves[target_elf]

            # remove target elf
            self.delete_target_elf(previous_elf, target_elf)

            current_elf_index = self.next_elves[current_elf_index]
            elves_remaining -= 1
        return current_elf_index + 1

    def delete_target_elf(self, previous_elf, target_elf):
        next_elf = self.next_elves[target_elf]
        self.next_elves[previous_elf] = next_elf
        target_elf %= len(self.next_elves)
