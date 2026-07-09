"""
Connected Components skeleton -- just fill in connected_components() below.

Idea: a "connected component" is a group of vertices that can all reach
each other. This is the UNDIRECTED graph version (for directed graphs,
the equivalent concept is "Strongly Connected Components" -- a harder,
separate topic using Kosaraju's or Tarjan's algorithm).

Approach:
- Go through every vertex in the graph.
- If it hasn't been visited yet, it's the start of a NEW component --
  run DFS or BFS from it, collect everything reachable, mark all visited.
- Repeat until every vertex has been visited.
- Return a list of components (each component is a list of vertices).
"""

from collections import deque


class Graph:
    def __init__(self):
        self.adjacent_list = {}   # undirected graph

    def add_vertex(self, v):
        if v not in self.adjacent_list:
            self.adjacent_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacent_list[u].append(v)
        self.adjacent_list[v].append(u)

    def display(self):
        return self.adjacent_list


# ---------------------------------------------------------
# YOUR CODE HERE
# ---------------------------------------------------------
# via bfs
def connected_components_via_bfs(graph):
    visited = set()
    def bfs(node):
        queue = deque([node])
        visited.add(node)
        component =[]
        while queue:
            item  = queue.popleft()
            component.append(item)
            for neighbour in graph.adjacent_list[item]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return component

    order = []
    for vertex in graph.adjacent_list:
        if vertex not in visited:
            order.append(bfs(vertex))
    return order

def connected_components_via_dfs(graph):
    visited = set()

    def dfs(node):
        stack = [node]
        component = []
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.append(current)
                for neighbour in graph.adjacent_list[current]:
                    if neighbour not in visited:
                        stack.append(neighbour)
        return component

    order = []
    for vertex in graph.adjacent_list:
        if vertex not in visited:
            order.append(dfs(vertex))
    return order


# ---------------------------------------------------------
# HELPER (do not need to modify)
# ---------------------------------------------------------

def normalize(components):
    """Sort components and their contents so comparison ignores ordering."""
    return sorted(sorted(component) for component in components)


# ---------------------------------------------------------
# TEST CASES -- do not need to modify below this line
# ---------------------------------------------------------

def run_tests(connected_components):
    # Test 1: fully connected graph -- one single component
    #     A - B - C
    #     |
    #     D
    g1 = Graph()
    g1.add_edge("A", "B")
    g1.add_edge("B", "C")
    g1.add_edge("A", "D")

    result1 = connected_components(g1)
    print("Test 1 graph:", g1.display())
    print("Components:", result1)
    print("Expected: one component containing A, B, C, D")
    print("Match:", normalize(result1) == normalize([["A", "B", "C", "D"]]))
    print()

    # Test 2: two separate components
    #     A - B        C - D
    g2 = Graph()
    g2.add_edge("A", "B")
    g2.add_edge("C", "D")

    result2 = connected_components(g2)
    print("Test 2 graph:", g2.display())
    print("Components:", result2)
    print("Match:", normalize(result2) == normalize([["A", "B"], ["C", "D"]]))
    print()

    # Test 3: fully disconnected graph -- every vertex is its own component
    g3 = Graph()
    g3.add_vertex("A")
    g3.add_vertex("B")
    g3.add_vertex("C")

    result3 = connected_components(g3)
    print("Test 3 graph:", g3.display())
    print("Components:", result3)
    print("Match:", normalize(result3) == normalize([["A"], ["B"], ["C"]]))
    print()

    # Test 4: single node, no edges
    g4 = Graph()
    g4.add_vertex("X")

    result4 = connected_components(g4)
    print("Test 4 graph:", g4.display())
    print("Components:", result4)
    print("Match:", normalize(result4) == normalize([["X"]]))
    print()

    # Test 5: three separate components of different sizes
    #     A - B - C        D - E        F
    g5 = Graph()
    g5.add_edge("A", "B")
    g5.add_edge("B", "C")
    g5.add_edge("D", "E")
    g5.add_vertex("F")

    result5 = connected_components(g5)
    print("Test 5 graph:", g5.display())
    print("Components:", result5)
    print("Match:", normalize(result5) == normalize([["A", "B", "C"], ["D", "E"], ["F"]]))
    print()

    # Test 6: empty graph
    g6 = Graph()

    result6 = connected_components(g6)
    print("Test 6 graph:", g6.display())
    print("Components:", result6)
    print("Match:", result6 == [])


if __name__ == "__main__":
    run_tests(connected_components_via_dfs)
    run_tests(connected_components_via_bfs)