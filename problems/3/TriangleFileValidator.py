def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return c < a + b


class TriangleFileValidator():
    def get_number_of_valid_triangles(self, input_file):
        valid_count = 0
        for line in input_file:
            putative_triangle = [int(x) for x in line.split()]
            if is_valid_triangle(putative_triangle):
                valid_count += 1
        return valid_count
