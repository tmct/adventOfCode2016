from collections import deque


def get_adjacent_states(current_node):
    x, y = current_node
    return (x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)


class Maze:
    def __init__(self, seed):
        self.seed = seed
        self.visited_nodes = {}
        self.nodes_to_examine = deque()
        self.bad_states = set()

    def get_shortest_path(self, start_pos, end_pos):
        self.visited_nodes[start_pos] = 0
        self.nodes_to_examine.append(start_pos)

        while True:
            current_node = self.nodes_to_examine.popleft()
            current_distance = self.visited_nodes[current_node]
            for new_node in self.get_valid_adjacent_states(current_node):
                self.visited_nodes[new_node] = current_distance + 1
                self.nodes_to_examine.append(new_node)
                if new_node == end_pos:
                    return self.visited_nodes[new_node]

    def find_nodes_n_away(self, start_pos, max_steps):
        self.visited_nodes[start_pos] = 0
        self.nodes_to_examine.append(start_pos)

        while len(self.nodes_to_examine):
            current_node = self.nodes_to_examine.popleft()
            current_distance = self.visited_nodes[current_node]
            for new_node in self.get_valid_adjacent_states(current_node):
                if current_distance < max_steps:
                    self.visited_nodes[new_node] = current_distance + 1
                    self.nodes_to_examine.append(new_node)
        return len(self.visited_nodes)

    def is_valid_position(self, position):
        x, y = position
        if x < 0 or y < 0:
            return False
        check = x * x \
                + 3 * x \
                + 2 * x * y \
                + y \
                + y * y \
                + self.seed

        binary_rep = "{0:b}".format(check)
        return not (binary_rep.count('1') & 1)

    def get_valid_adjacent_states(self, current_node):
        adjacent_states = get_adjacent_states(current_node)
        return (state for state in adjacent_states if self.is_valid_unvisited_state(state))

    def is_valid_unvisited_state(self, state):
        return state not in self.visited_nodes and self.is_valid_position(state)

