number_of_levels = 4
from itertools import cycle, islice, combinations


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


class State:
    def __init__(self, lift_level, chip_levels, generator_levels):
        self.lift_level = lift_level
        self.chip_levels = chip_levels
        self.generator_levels = generator_levels
        self._lift_level_gens = None
        self._lift_level_chips = None
        self._is_safe = None

    @property
    def is_safe(self):
        if self._is_safe is None:
            levels_with_generators = self.get_generator_levels()
            unpowered_chips = self.get_unpowered_chips()
            unpowered_chip_levels = self.get_unpowered_chip_levels(unpowered_chips)
            self._is_safe = levels_with_generators.isdisjoint(unpowered_chip_levels)
        return self._is_safe


    def get_unpowered_chip_levels(self, unpowered_chips):
        return {chip_level for index, chip_level in enumerate(self.chip_levels) if
                unpowered_chips[index]}

    def get_unpowered_chips(self):
        return [chip_level != generator_level for chip_level, generator_level in
                zip(self.chip_levels, self.generator_levels)]

    def get_generator_levels(self):
        return {level_index for level_index in range(number_of_levels) if
                level_index in self.generator_levels}

    def adjacent_safe_states(self):
        self._lift_level_gens = {generator for generator, level in enumerate(self.generator_levels) if
                                 level == self.lift_level}
        self._lift_level_chips = {chip for chip, level in enumerate(self.chip_levels) if level == self.lift_level}
        # iterate over up/down and taking all things on this level, one or two from all, and must be safe
        # up first
        return {state for state in self.adjacent_states if state.is_safe}

    @property
    def adjacent_states(self):
        # iterate over up/down and taking all things on this level, one or two from all, and must be safe
        # up first
        return set(self.adjacent_up_states() + self.adjacent_down_states())  # todo remove most sets

    def adjacent_up_states(self):
        next_lift_level = self.lift_level + 1
        if next_lift_level == number_of_levels:
            return []
        return self.raise_single_chip_states(self._lift_level_chips) + self.raise_single_gen_states(
            self._lift_level_gens) + self.raise_double_chip_states(
            self._lift_level_chips) + self.raise_double_gen_states(
            self._lift_level_gens) + self.raise_chip_and_gen_states(self._lift_level_chips, self._lift_level_gens)

    def raise_single_chip_states(self, chips):
        return [self.raise_chip(chip) for chip in chips]

    def raise_double_chip_states(self, chips):
        return [self.raise_two_chips(chip1, chip2) for chip1, chip2 in combinations(chips, 2)]

    def raise_double_gen_states(self, gens):
        return [self.raise_two_gens(gen1, gen2) for gen1, gen2 in combinations(gens, 2)]

    def raise_two_gens(self, gen1, gen2):
        new_generator_levels = list(self.generator_levels)
        new_generator_levels[gen1] += 1
        new_generator_levels[gen2] += 1
        return State(self.lift_level + 1,
                     self.chip_levels,
                     tuple(new_generator_levels))

    def raise_two_chips(self, chip1, chip2):
        new_chip_levels = list(self.chip_levels)
        new_chip_levels[chip1] += 1
        new_chip_levels[chip2] += 1
        return State(self.lift_level + 1,
                     tuple(new_chip_levels),
                     self.generator_levels)

    def raise_single_gen_states(self, gens):
        return [self.raise_generator(generator) for generator in gens]

    def raise_chip_and_gen_states(self, chips, gens):
        return [self.raise_chip_and_gen(chip, gen) for gen in gens for chip in chips]

    def raise_chip(self, chip):
        new_chip_levels = list(self.chip_levels)
        new_chip_levels[chip] += 1
        return State(self.lift_level + 1,
                     tuple(new_chip_levels),
                     self.generator_levels)

    def raise_generator(self, generator):
        new_generator_levels = list(self.generator_levels)
        new_generator_levels[generator] += 1
        return State(self.lift_level + 1,
                     self.chip_levels,
                     tuple(new_generator_levels))

    def raise_chip_and_gen(self, chip, gen):
        new_chip_levels = list(self.chip_levels)
        new_chip_levels[chip] += 1
        new_generator_levels = list(self.generator_levels)
        new_generator_levels[gen] += 1
        return State(self.lift_level + 1,
                     tuple(new_chip_levels),
                     tuple(new_generator_levels))

    def __repr__(self):
        res = ''
        for level in range(number_of_levels):
            res += str(level + 1) + ' '
            lift_char = '.'
            if self.lift_level == number_of_levels - level - 1:
                lift_char = 'E'
            res += lift_char + ' '
            for value in roundrobin(self.generator_levels, self.chip_levels):
                char = '.'
                if value == number_of_levels - level - 1:
                    char = '*'
                res += char + ' '
            res += '\n'
        return res

    def adjacent_down_states(self):
        next_lift_level = self.lift_level - 1
        if next_lift_level == -1:
            return []

        return self.lower_single_chip_states(self._lift_level_chips) + self.lower_single_gen_states(
            self._lift_level_gens) + self.lower_double_chip_states(
            self._lift_level_chips) + self.lower_double_gen_states(
            self._lift_level_gens) + self.lower_chip_and_gen_states(self._lift_level_chips, self._lift_level_gens)

    def lower_single_chip_states(self, chips):
        return [self.lower_chip(chip) for chip in chips]

    def lower_double_chip_states(self, chips):
        return [self.lower_two_chips(chip1, chip2) for chip1, chip2 in combinations(chips, 2)]

    def lower_double_gen_states(self, gens):
        return [self.lower_two_gens(gen1, gen2) for gen1, gen2 in combinations(gens, 2)]

    def lower_two_gens(self, gen1, gen2):
        new_generator_levels = list(self.generator_levels)
        new_generator_levels[gen1] -= 1
        new_generator_levels[gen2] -= 1
        return State(self.lift_level - 1,
                     self.chip_levels,
                     tuple(new_generator_levels))

    def lower_two_chips(self, chip1, chip2):
        new_chip_levels = list(self.chip_levels)
        new_chip_levels[chip1] -= 1
        new_chip_levels[chip2] -= 1
        return State(self.lift_level - 1,
                     tuple(new_chip_levels),
                     self.generator_levels)

    def lower_single_gen_states(self, gens):
        return [self.lower_generator(generator) for generator in gens]

    def lower_chip_and_gen_states(self, chips, gens):
        return [self.lower_chip_and_gen(chip, gen) for gen in gens for chip in chips]

    def lower_chip(self, chip):
        new_chip_levels = list(self.chip_levels)
        new_chip_levels[chip] -= 1
        return State(self.lift_level - 1,
                     tuple(new_chip_levels),
                     self.generator_levels)

    def lower_generator(self, generator):
        new_generator_levels = list(self.generator_levels)
        new_generator_levels[generator] -= 1
        return State(self.lift_level - 1,
                     self.chip_levels,
                     tuple(new_generator_levels))

    def lower_chip_and_gen(self, chip, gen):
        new_chip_levels = list(self.chip_levels)
        new_chip_levels[chip] -= 1
        new_generator_levels = list(self.generator_levels)
        new_generator_levels[gen] -= 1
        return State(self.lift_level - 1,
                     tuple(new_chip_levels),
                     tuple(new_generator_levels))

    def __key(self):
        return self.lift_level, tuple(sorted(zip(self.chip_levels, self.generator_levels)))

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())
