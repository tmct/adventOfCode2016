def contains_abba(seq):
    return any(is_abba_element(seq[i:i+4]) for i in range(len(seq) - 3))


def get_abas(seq):
    return set(seq[i:i+3] for i in range(len(seq) - 2) if is_aba_element(seq[i:i+3]))


def is_abba_element(element):
    return element[1] == element[2]\
           and element[0] == element[3]\
           and element[0] != element[1]


def is_aba_element(element):
    return element[0] == element[2]\
           and element[0] != element[1]


def get_corresponding_aba(aba):
    return aba[1] + aba[0] + aba[1]


class IP:
    def __init__(self, address):
        self.address = address
        self.non_hypernet_sequences = []
        self.hypernet_sequences = []
        self.parse_address(address)

    @property
    def supports_tls(self):
        return any(contains_abba(seq) for seq in self.non_hypernet_sequences)\
               and not any(contains_abba(seq) for seq in self.hypernet_sequences)

    def parse_address(self, address):
        split_address = address.replace(']', '[').split('[')
        self.non_hypernet_sequences = split_address[::2]
        self.hypernet_sequences = split_address[1::2]

    @property
    def supports_ssl(self):
        non_hypernet_aba_sets = [get_abas(seq) for seq in self.non_hypernet_sequences]
        non_hypernet_abas = frozenset().union(*non_hypernet_aba_sets)
        corresponding_abas = set(get_corresponding_aba(aba) for aba in non_hypernet_abas)
        hypernet_aba_sets = [get_abas(seq) for seq in self.hypernet_sequences]
        hypernet_abas = frozenset().union(*hypernet_aba_sets)
        return not hypernet_abas.isdisjoint(corresponding_abas)