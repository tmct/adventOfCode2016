from collections import deque


class BreadthFirstSearch:
    def __init__(self, limit = None):
        self.limit = limit
        self.visited_nodes = {}
        self.nodes_to_examine = deque()

    def find_distance(self, root_state, target_state):
        self.visited_nodes[root_state] = {'parent': None, 'distance': 0}
        self.nodes_to_examine.append(root_state)

        while not self.limit or len(self.nodes_to_examine) < self.limit:
            current_node = self.nodes_to_examine.popleft()
            current_distance = self.visited_nodes[current_node]['distance']
            for new_node in current_node.adjacent_safe_states():
                if new_node not in self.visited_nodes:
                    self.visited_nodes[new_node] = {'parent': current_node, 'distance': current_distance + 1}
                    self.nodes_to_examine.append(new_node)
                    if new_node == target_state:
                        print("UTTER SUCCESS!")
                        self.print_intermediate_steps(root_state, new_node)
                        return self.visited_nodes[new_node]['distance']

    def print_intermediate_steps(self, start_node, end_node):
        journey = [end_node]
        current_node = end_node
        while start_node not in journey:
            current_node = self.visited_nodes[current_node]['parent']
            journey.append(current_node)
        journey = journey[::-1]
        for node in journey:
            print(node)
