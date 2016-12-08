from Solver1a import Solver1a


def main():
    solver = Solver1a()
    with open('input.txt', 'r') as input_file:
        directions_string = input_file.read().replace('\n', '')
    solution = solver.get_shortest_path(directions_string)
    print(solution)

if __name__ == '__main__':
    main()