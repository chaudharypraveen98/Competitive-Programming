"""
Cycle Detection (UNDIRECTED graphs) skeleton -- fill in has_cycle_undirected() below.

Naive idea "if I revisit a visited node, it's a cycle" is WRONG here --
because going back along the same edge you just came from (A -> B, then
checking B's neighbor A) looks like a revisit but is NOT a cycle.

Fix: track the PARENT of each node in the DFS. When checking a neighbor,
skip it if it's the parent you just came from. If you find any OTHER
already-visited neighbor, that's a genuine cycle.

Remember to handle disconnected graphs -- check every component,
not just one DFS from a single start node.
"""


class Graph:
    def __init__(self):
        self.adjacent_list = {}   # undirected only

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

def has_cycle_undirected(graph):
    """
    Return True if the UNDIRECTED graph contains a cycle, else False.
    Hint: DFS with parent-tracking. Handle disconnected graphs.
    """
    visited = set()
    def dfs(node, stack=None, parent =None):
        if stack is None:
            stack = set()
        visited.add(node)

        stack.add(node)
        for neighbour in graph.adjacent_list[node]:
            if neighbour in stack and parent!= neighbour:
                return True
            if neighbour not in visited and dfs(neighbour, stack, node):
                return True
        stack.remove(node)
        return False
    for vertex in graph.adjacent_list:
        if vertex not in visited and dfs(vertex):
            return True
    return False

# ---------------------------------------------------------
# TEST CASES -- do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    print("===== Testing has_cycle_undirected =====")

    # Test 1: simple triangle -- has a cycle
    #     A - B - C - A
    g1 = Graph()
    g1.add_edge("A", "B")
    g1.add_edge("B", "C")
    g1.add_edge("C", "A")
    print("Test 1 graph:", g1.display())
    print("Has cycle:", has_cycle_undirected(g1), "(expected: True)")
    print()

    # Test 2: simple tree -- no cycle (the classic parent-trap case:
    # naive "revisit = cycle" logic would wrongly say True here)
    #     A - B - C
    #     |
    #     D
    g2 = Graph()
    g2.add_edge("A", "B")
    g2.add_edge("B", "C")
    g2.add_edge("A", "D")
    print("Test 2 graph:", g2.display())
    print("Has cycle:", has_cycle_undirected(g2), "(expected: False)")
    print()

    # Test 3: disconnected graph, cycle in one component only
    #     A - B          C - D - E - C   (cycle here)
    g3 = Graph()
    g3.add_edge("A", "B")
    g3.add_edge("C", "D")
    g3.add_edge("D", "E")
    g3.add_edge("E", "C")
    print("Test 3 graph:", g3.display())
    print("Has cycle:", has_cycle_undirected(g3), "(expected: True)")
    print()

    # Test 4: disconnected graph, no cycle anywhere
    #     A - B          C - D
    g4 = Graph()
    g4.add_edge("A", "B")
    g4.add_edge("C", "D")
    print("Test 4 graph:", g4.display())
    print("Has cycle:", has_cycle_undirected(g4), "(expected: False)")
    print()

    # Test 5: single node, no edges
    g5 = Graph()
    g5.add_vertex("X")
    print("Test 5 graph:", g5.display())
    print("Has cycle:", has_cycle_undirected(g5), "(expected: False)")
    print()

    # Test 6: single edge only (the simplest parent-trap case)
    #     A - B
    g6 = Graph()
    g6.add_edge("A", "B")
    print("Test 6 graph:", g6.display())
    print("Has cycle:", has_cycle_undirected(g6), "(expected: False)")
    print()

    # Test 7: larger graph, cycle formed by a "shortcut" edge
    #     A - B - C - D
    #         |_______|        (B - D shortcut creates a cycle B-C-D-B)
    g7 = Graph()
    g7.add_edge("A", "B")
    g7.add_edge("B", "C")
    g7.add_edge("C", "D")
    g7.add_edge("B", "D")
    print("Test 7 graph:", g7.display())
    print("Has cycle:", has_cycle_undirected(g7), "(expected: True)")


if __name__ == "__main__":
    run_tests()