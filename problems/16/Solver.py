swap = {'1':'0', '0':'1'}


def get_checksum(string):
    if len(string) % 2:
        return string
    checksum = []
    for i in range(0, len(string), 2):
        checksum.append(str(int(string[i] == string[i + 1])))
    return get_checksum(''.join(checksum))


class Solver:
    def solve(self, length_required, initial_state):
        a = initial_state
        while len(a) < length_required:
            #print(len(a))
            b = ''.join(swap[dig] for dig in a[::-1])
            a = a + '0' + b
        disk_data = a[:length_required]
        #print(disk_data)

        checksum = get_checksum(disk_data)
        return checksum


