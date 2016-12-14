import re
import functools
import operator
from Bot import Bot


def product(iterable):
    return functools.reduce(operator.mul, iterable, 1)


value_instruction_regex = r'value (\d+) goes to bot (\d+)'
compare_instruction_basic_regex = r'^bot (\d+)'
compare_instruction_regex = r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)'


class BotCollective:
    def __init__(self):
        self.bots = []
        self.outputs = []

    def add_instruction(self, instruction_string):
        if not instruction_string:
            return
        value_match = re.search(value_instruction_regex, instruction_string)
        if value_match:
            chip_value = int(value_match.group(1))
            bot_index = int(value_match.group(2))
            self.give_starting_chip_to_bot(chip_value, bot_index)
            return
        compare_match = re.search(compare_instruction_basic_regex, instruction_string)
        if compare_match:
            subject_bot_index = int(compare_match.group(1))
            self.add_compare_rule(subject_bot_index, instruction_string)
            return
        raise Exception('line not matched: {}'.format(instruction_string))

    def give_starting_chip_to_bot(self, chip_value, bot_index):
        self.ensure_enough_bots(bot_index)
        self.bots[bot_index].give_chip(chip_value)

    def ensure_enough_bots(self, bot_index):
        number_bots = len(self.bots)
        if number_bots <= bot_index:
            for i in range(number_bots, bot_index + 1):
                self.bots.append(Bot(i))

    def ensure_enough_outputs(self, output_index):
        number_outputs = len(self.outputs)
        if number_outputs <= output_index:
            for i in range(number_outputs, output_index + 1):
                self.outputs.append(Bot(i))

    def add_compare_rule(self, subject_bot_index, compare_string):
        self.ensure_enough_bots(subject_bot_index)
        self.bots[subject_bot_index].add_compare_rule(compare_string)

    def find_comparer(self, firstCompareValue, secondCompareValue):
        further_distribution_needed = True
        while further_distribution_needed:
            further_distribution_needed = False
            for bot in self.bots:
                if bot.ready_to_sort:
                    self.distribute_chips(bot.compare_string, bot.low_chip, bot.high_chip)
                    bot.take_chips()
                    further_distribution_needed = True
        return next(
            i for i, bot in enumerate(self.bots) if
            bot.compared_chips and set(bot.compared_chips) == {firstCompareValue, secondCompareValue})

    def distribute_chips(self, compare_string, low_chip, high_chip):
        compare_match = re.search(compare_instruction_regex, compare_string)
        if not compare_match:
            raise Exception('Compare string not parsed correctly')
        subject_bot_index = int(compare_match.group(1))
        low_recipient_type = compare_match.group(2)
        low_recipient_index = int(compare_match.group(3))
        high_recipient_type = compare_match.group(4)
        high_recipient_index = int(compare_match.group(5))
        self.distribute_chip(low_chip, low_recipient_type, low_recipient_index)
        self.distribute_chip(high_chip, high_recipient_type, high_recipient_index)

    def distribute_chip(self, chip_value, recipient_type, recipient_index):
        if recipient_type == 'bot':
            self.ensure_enough_bots(recipient_index)
            self.bots[recipient_index].give_chip(chip_value)
        elif recipient_type == 'output':
            self.ensure_enough_outputs(recipient_index)
            self.outputs[recipient_index].give_chip(chip_value)
        else:
            raise Exception('unrecognised recipient type, {}'.format(recipient_type))

    def get_first_three_outputs_product(self):
        further_distribution_needed = True
        while further_distribution_needed:
            further_distribution_needed = False
            for bot in self.bots:
                if bot.ready_to_sort:
                    self.distribute_chips(bot.compare_string, bot.low_chip, bot.high_chip)
                    bot.take_chips()
                    further_distribution_needed = True
        return product(output.only_chip for output in self.outputs[:3])
