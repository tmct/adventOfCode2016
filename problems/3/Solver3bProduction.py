from VerticalTriangleFileValidator import VerticalTriangleFileValidator


def main():
    with open('input.txt', 'r') as input_file:
        number_valid_triangles = VerticalTriangleFileValidator().get_number_of_valid_triangles(input_file)
        print(number_valid_triangles)


if __name__ == '__main__':
    main()
