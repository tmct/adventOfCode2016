class Solver:
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
        elves = list(range(1, start_number + 1))
        current_elf_index = 0
        while len(elves) > 1:
            jump_distance = len(elves) // 2
            target_elf = jump_distance + current_elf_index
            if target_elf >= len(elves):
                del elves[target_elf - len(elves)]
                current_elf_index -= 1
            else:
                del elves[target_elf]
            current_elf_index += 1
            current_elf_index %= len(elves)

        return elves[current_elf_index]
