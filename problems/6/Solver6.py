def most_common(lst):
    return max(set(lst), key=lst.count)


def least_common(lst):
    return min(set(lst), key=lst.count)


class Solver6:
    def __init__(self, input_file_name):
        with open(input_file_name, 'r') as message_file:
            self.message_file_content = message_file.readlines()

    def get_message(self):
        columns = list(''.join(x) for x in zip(*self.message_file_content))[:-1]
        most_common_chars = (most_common(x) for x in columns)
        return ''.join(most_common_chars)

    def get_message_using_modified_code(self):
        columns = list(''.join(x) for x in zip(*self.message_file_content))[:-1]
        least_common_chars = (least_common(x) for x in columns)
        return ''.join(least_common_chars)