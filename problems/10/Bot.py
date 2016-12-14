class Bot:
    def __init__(self, index):
        self.chips = set()
        self.index = index
        self.compare_string = None
        self.compared_chips = None

    @property
    def low_chip(self):
        return min(self.chips)

    @property
    def high_chip(self):
        return max(self.chips)

    @property
    def only_chip(self):
        if len(self.chips) > 1:
            raise Exception('More than one chip!')
        return next(iter(self.chips))

    def give_chip(self, chip_value):
        if chip_value in self.chips:
            raise Exception('Bot {} already has value {}', self.index, chip_value)
        self.chips.add(chip_value)

    @property
    def ready_to_sort(self):
        return len(self.chips) == 2

    def add_compare_rule(self, compare_string):
        if self.compare_string:
            raise Exception('Bot {} already has compare rule', self.index)
        self.compare_string = compare_string

    def take_chips(self):
        self.compared_chips = sorted(self.chips)
        self.chips.clear()