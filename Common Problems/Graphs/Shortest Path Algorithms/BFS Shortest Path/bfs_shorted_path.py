"""
BFS Shortest Path skeleton — just fill in the shortest_path_bfs() function below.

Note: this is different from plain BFS traversal.
- Plain BFS returns the *order* nodes are visited in.
- BFS shortest path returns the *actual path* (list of nodes) from start to target,
  using the fewest number of edges (only valid for UNWEIGHTED graphs).

Hint: track each node's parent as you discover it, then walk backwards from
target to start using those parent links once target is found.
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

def shortest_path_bfs(graph, start, target):
    """
    Return the shortest path (list of nodes, start to target inclusive)
    in an UNWEIGHTED graph using BFS.

    Return None if target is unreachable from start.
    If start == target, return [start].
    """
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == target:
            return path
        for neighbor in graph.adjacent_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


# ---------------------------------------------------------
# TEST CASES — do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    # Test 1: simple undirected graph, one clear shortest path
    #     A - B - D
    #     |
    #     C
    g1 = Graph(directed=False)
    g1.add_edge("A", "B")
    g1.add_edge("A", "C")
    g1.add_edge("B", "D")

    print("Test 1 graph:", g1.display())
    print("Shortest path A -> D:", shortest_path_bfs(g1, "A", "D"))
    # expected: ['A', 'B', 'D']
    print()

    # Test 2: start == target
    print("Shortest path A -> A:", shortest_path_bfs(g1, "A", "A"))
    # expected: ['A']
    print()

    # Test 3: target unreachable (disconnected graph)
    #     A - B      C - D
    g3 = Graph(directed=False)
    g3.add_edge("A", "B")
    g3.add_edge("C", "D")

    print("Test 3 graph:", g3.display())
    print("Shortest path A -> D:", shortest_path_bfs(g3, "A", "D"))
    # expected: None
    print()

    # Test 4: multiple possible paths, must pick the SHORTEST (fewest edges)
    #     A - B - C - D      (3 edges)
    #     A ------- D        (1 edge, direct)
    g4 = Graph(directed=False)
    g4.add_edge("A", "B")
    g4.add_edge("B", "C")
    g4.add_edge("C", "D")
    g4.add_edge("A", "D")

    print("Test 4 graph:", g4.display())
    print("Shortest path A -> D:", shortest_path_bfs(g4, "A", "D"))
    # expected: ['A', 'D']   (direct edge is fewer hops than going through B, C)
    print()

    # Test 5: directed graph, path only exists in one direction
    #     A -> B -> C
    #     D -> C          (D can reach C, but C cannot reach back to A/B/D)
    g5 = Graph(directed=True)
    g5.add_edge("A", "B")
    g5.add_edge("B", "C")
    g5.add_edge("D", "C")

    print("Test 5 graph:", g5.display())
    print("Shortest path A -> C:", shortest_path_bfs(g5, "A", "C"))
    # expected: ['A', 'B', 'C']
    print("Shortest path C -> A:", shortest_path_bfs(g5, "C", "A"))
    # expected: None  (no outgoing edges from C)
    print()

    # Test 6: larger graph with multiple branches, verify fewest-hops logic
    #        A
    #      / | \
    #     B  C  D
    #     |     |
    #     E     F
    #      \   /
    #        G
    g6 = Graph(directed=False)
    g6.add_edge("A", "B")
    g6.add_edge("A", "C")
    g6.add_edge("A", "D")
    g6.add_edge("B", "E")
    g6.add_edge("D", "F")
    g6.add_edge("E", "G")
    g6.add_edge("F", "G")

    print("Test 6 graph:", g6.display())
    print("Shortest path A -> G:", shortest_path_bfs(g6, "A", "G"))
    # expected: either ['A', 'B', 'E', 'G'] or ['A', 'D', 'F', 'G'] -- both length 4, both valid
    print("Shortest path A -> X (nonexistent node):", shortest_path_bfs(g6, "A", "X"))
    # expected: None


if __name__ == "__main__":
    run_tests()