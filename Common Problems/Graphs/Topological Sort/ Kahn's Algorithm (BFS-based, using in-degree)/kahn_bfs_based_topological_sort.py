"""
Topological Sort -- REFERENCE SOLUTIONS (Kahn's + DFS-based)

Use this to check your own attempt in topological_sort_skeleton.py.
Same Graph class and test cases as the skeleton file.
"""

from collections import deque


class Graph:
    def __init__(self):
        self.adjacent_list = {}   # vertex -> list of neighbors (directed only)

    def add_vertex(self, v):
        if v not in self.adjacent_list:
            self.adjacent_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacent_list[u].append(v)

    def display(self):
        return self.adjacent_list

def topo_sort_kahn(graph):
    """
    Return a list of vertices in valid topological order using Kahn's algorithm.
    Raise ValueError("Graph has a cycle") if no valid ordering exists.
    """
    # Step 1: compute in-degree for every vertex
    in_degree = {v: 0 for v in graph.adjacent_list}
    for u in graph.adjacent_list:
        for v in graph.adjacent_list[u]:
            in_degree[v] += 1

    # Step 2: start with all vertices that have no incoming edges
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        # "remove" node's outgoing edges by decrementing neighbor in-degrees
        for neighbor in graph.adjacent_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: if we didn't process every vertex, some vertices never
    # reached in-degree 0 -- meaning a cycle exists among them
    if len(order) != len(graph.adjacent_list):
        raise ValueError("Graph has a cycle")

    return order

# ---------------------------------------------------------
# HELPER
# ---------------------------------------------------------

def is_valid_topo_order(graph, order):
    """
    Checks whether `order` is a VALID topological order for `graph` --
    i.e. for every edge u -> v, u appears before v in `order`.
    """
    position = {node: i for i, node in enumerate(order)}
    if set(position) != set(graph.adjacent_list):
        return False
    for u in graph.adjacent_list:
        for v in graph.adjacent_list[u]:
            if position[u] > position[v]:
                return False
    return True


# ---------------------------------------------------------
# TEST CASES
# ---------------------------------------------------------

def run_tests(topo_sort_fn, label):
    print(f"===== Testing {label} =====")

    g1 = Graph()
    g1.add_edge("A", "B")
    g1.add_edge("A", "C")
    g1.add_edge("B", "D")
    g1.add_edge("C", "D")
    order1 = topo_sort_fn(g1)
    print("Test 1 graph:", g1.display())
    print("Topo order:", order1, "-> valid?", is_valid_topo_order(g1, order1))
    print()

    g2 = Graph()
    g2.add_edge("A", "B")
    g2.add_edge("B", "C")
    g2.add_edge("C", "D")
    order2 = topo_sort_fn(g2)
    print("Test 2 graph:", g2.display())
    print("Topo order:", order2, "-> valid?", is_valid_topo_order(g2, order2))
    print()

    g3 = Graph()
    g3.add_edge("A", "B")
    g3.add_edge("C", "D")
    order3 = topo_sort_fn(g3)
    print("Test 3 graph:", g3.display())
    print("Topo order:", order3, "-> valid?", is_valid_topo_order(g3, order3))
    print()

    g4 = Graph()
    g4.add_vertex("X")
    order4 = topo_sort_fn(g4)
    print("Test 4 graph:", g4.display())
    print("Topo order:", order4, "-> valid?", is_valid_topo_order(g4, order4))
    print()

    g5 = Graph()
    g5.add_edge("A", "B")
    g5.add_edge("A", "C")
    g5.add_edge("A", "D")
    g5.add_edge("B", "E")
    g5.add_edge("C", "E")
    g5.add_edge("D", "E")
    order5 = topo_sort_fn(g5)
    print("Test 5 graph:", g5.display())
    print("Topo order:", order5, "-> valid?", is_valid_topo_order(g5, order5))
    print()

    g6 = Graph()
    g6.add_edge("A", "B")
    g6.add_edge("B", "C")
    g6.add_edge("C", "A")
    print("Test 6 graph:", g6.display())
    try:
        result = topo_sort_fn(g6)
        print("ERROR: expected a ValueError, but got:", result)
    except ValueError as e:
        print("Correctly raised ValueError:", e)
    print()


if __name__ == "__main__":
    run_tests(topo_sort_kahn, "Kahn's Algorithm (BFS)")