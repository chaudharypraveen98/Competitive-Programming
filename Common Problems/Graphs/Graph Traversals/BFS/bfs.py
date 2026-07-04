"""
BFS skeleton — just fill in the bfs() function below.
"""

from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacent_list = {}

    def add_vertex(self, v):
        if v not in self.adjacent_list:
            self.adjacent_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacent_list[u].append(v)
        if not self.directed:
            self.adjacent_list[v].append(u)

    def display(self):
        return self.adjacent_list


# ---------------------------------------------------------
# YOUR CODE HERE
# ---------------------------------------------------------

def bfs(graph, start):
    order = []
    visited = {start}          # mark start visited immediately
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.adjacent_list[node]:
            if neighbour not in visited:
                visited.add(neighbour)   # mark visited when pushing, not popping
                queue.append(neighbour)
    return order


# ---------------------------------------------------------
# TEST CASES — do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    # Test 1: simple undirected graph
    #     A - B - D
    #     |
    #     C
    g1 = Graph(directed=False)
    g1.add_edge("A", "B")
    g1.add_edge("A", "C")
    g1.add_edge("B", "D")

    print("Test 1 graph:", g1.display())
    print("BFS from A:", bfs(g1, "A"))   # expected: A, B, C, D
    print()

    # Test 2: disconnected graph
    #     A - B      C - D
    g2 = Graph(directed=False)
    g2.add_edge("A", "B")
    g2.add_edge("C", "D")

    print("Test 2 graph:", g2.display())
    print("BFS from A:", bfs(g2, "A"))   # expected: A, B  (C, D unreachable from A)
    print()

    # Test 3: directed graph with a cycle
    #     A -> B -> C -> A   (cycle)
    #     B -> D
    g3 = Graph(directed=True)
    g3.add_edge("A", "B")
    g3.add_edge("B", "C")
    g3.add_edge("C", "A")
    g3.add_edge("B", "D")

    print("Test 3 graph:", g3.display())
    print("BFS from A:", bfs(g3, "A"))   # expected: A, B, C, D  (visited set stops the cycle)
    print()

    # Test 4: single node, no edges
    g4 = Graph(directed=False)
    g4.add_vertex("X")

    print("Test 4 graph:", g4.display())
    print("BFS from X:", bfs(g4, "X"))   # expected: X
    print()

    # Test 5: larger graph, multiple branches
    #        A
    #      / | \
    #     B  C  D
    #     |     |
    #     E     F
    g5 = Graph(directed=False)
    g5.add_edge("A", "B")
    g5.add_edge("A", "C")
    g5.add_edge("A", "D")
    g5.add_edge("B", "E")
    g5.add_edge("D", "F")

    print("Test 5 graph:", g5.display())
    print("BFS from A:", bfs(g5, "A"))   # expected: A, B, C, D, E, F


if __name__ == "__main__":
    run_tests()