from Solver1b import Solver1b


def main():
    solver = Solver1b()
    with open('input.txt', 'r') as input_file:
        directions_string = input_file.read().replace('\n', '')
    solution = solver.get_distance_to_first_repeat_visit(directions_string)
    print(solution)

if __name__ == '__main__':
    main()