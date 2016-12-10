def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return c < a + b


class VerticalTriangleFileValidator():
    def get_number_of_valid_triangles(self, input_file):
        valid_count = 0
        while True:
            triangles_transposed = []
            for i in range(3):
                triangles_transposed.append([int(x) for x in input_file.readline().split()])
                if not triangles_transposed[-1]:
                    return valid_count
            triangles = [list(x) for x in zip(*triangles_transposed)]
            for putative_triangle in triangles:
                if is_valid_triangle(putative_triangle):
                    valid_count += 1
