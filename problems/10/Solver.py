from BotCollective import BotCollective


class Solver:
    def find_compare_bot(self, input_file_name, firstCompareValue, secondCompareValue):
        with open(input_file_name, 'r') as input_file:
            bot_collective = BotCollective()
            for line in input_file:
                bot_collective.add_instruction(line.strip())
            comparer_index = bot_collective.find_comparer(firstCompareValue, secondCompareValue)
            return comparer_index
