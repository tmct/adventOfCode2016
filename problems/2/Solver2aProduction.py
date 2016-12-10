from Solver2a import Solver2a


def main():
    solver = Solver2a()
    with open('input.txt', 'r') as input_file:
        instructions_string = input_file.read()
    code = solver.get_bathroom_code(instructions_string)
    print(code)

if __name__ == '__main__':
    main()