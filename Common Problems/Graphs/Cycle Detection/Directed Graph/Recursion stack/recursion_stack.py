"""
Cycle Detection (DIRECTED graphs) skeleton -- fill in has_cycle_directed() below.

Parent-tracking (used for undirected graphs) doesn't work here, since edges
are one-way -- "going back the way you came" isn't a meaningful concept.

Instead, use WHITE/GRAY/BLACK coloring + the recursion stack (same technique
as topo_sort_dfs, since a directed cycle is exactly what makes topological
sort impossible):
- WHITE = not yet visited
- GRAY  = currently in the active DFS recursion path (an ancestor of the
  node currently being explored)
- BLACK = fully explored (this node and everything reachable from it is done)

If, while exploring a node's neighbors, you find a neighbor that is GRAY,
you've found a back-edge pointing to an ancestor -- that's a cycle.
Finding a BLACK neighbor is fine -- it's already fully explored and safe.
"""


class Graph:
    def __init__(self):
        self.adjacent_list = {}   # directed only

    def add_vertex(self, v):
        if v not in self.adjacent_list:
            self.adjacent_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacent_list[u].append(v)

    def display(self):
        return self.adjacent_list


# ---------------------------------------------------------
# YOUR CODE HERE
# ---------------------------------------------------------

def has_cycle_directed(graph):
    """
    Return True if the DIRECTED graph contains a cycle, else False.
    Hint: WHITE/GRAY/BLACK coloring, same idea as topo_sort_dfs.
    Handle disconnected graphs -- check every component.
    """
    visited =set()
    def dfs(node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node) 

        for neighbour in graph.adjacent_list[node]:
            if neighbour in rec_stack:
                return True
            if neighbour not in visited and dfs(neighbour, visited, rec_stack):
                return True

        rec_stack.remove(node)
        return False
    
    for vertex in graph.adjacent_list:
        if vertex not in visited and dfs(vertex, visited, set()):
            return True
    return False


# ---------------------------------------------------------
# TEST CASES -- do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    print("===== Testing has_cycle_directed =====")

    # Test 1: simple directed cycle
    #     A -> B -> C -> A
    g1 = Graph()
    g1.add_edge("A", "B")
    g1.add_edge("B", "C")
    g1.add_edge("C", "A")
    print("Test 1 graph:", g1.display())
    print("Has cycle:", has_cycle_directed(g1), "(expected: True)")
    print()

    # Test 2: DAG, no cycle (the classic trap: A -> B and A -> C sharing
    # a descendant D is NOT a cycle just because D is reached twice)
    #     A -> B -> D
    #     A -> C -> D
    g2 = Graph()
    g2.add_edge("A", "B")
    g2.add_edge("A", "C")
    g2.add_edge("B", "D")
    g2.add_edge("C", "D")
    print("Test 2 graph:", g2.display())
    print("Has cycle:", has_cycle_directed(g2), "(expected: False)")
    print()

    # Test 3: disconnected graph, cycle in one component only
    #     A -> B          C -> D -> C   (cycle here)
    g3 = Graph()
    g3.add_edge("A", "B")
    g3.add_edge("C", "D")
    g3.add_edge("D", "C")
    print("Test 3 graph:", g3.display())
    print("Has cycle:", has_cycle_directed(g3), "(expected: True)")
    print()

    # Test 4: disconnected graph, no cycle anywhere
    g4 = Graph()
    g4.add_edge("A", "B")
    g4.add_edge("C", "D")
    print("Test 4 graph:", g4.display())
    print("Has cycle:", has_cycle_directed(g4), "(expected: False)")
    print()

    # Test 5: single node, no edges
    g5 = Graph()
    g5.add_vertex("X")
    print("Test 5 graph:", g5.display())
    print("Has cycle:", has_cycle_directed(g5), "(expected: False)")
    print()

    # Test 6: self-loop (A -> A) -- should count as a cycle
    g6 = Graph()
    g6.add_edge("A", "A")
    print("Test 6 graph:", g6.display())
    print("Has cycle:", has_cycle_directed(g6), "(expected: True)")
    print()

    # Test 7: back edge deep in a longer chain
    #     A -> B -> C -> D -> B   (cycle B-C-D-B, A is just a lead-in, not part of it)
    g7 = Graph()
    g7.add_edge("A", "B")
    g7.add_edge("B", "C")
    g7.add_edge("C", "D")
    g7.add_edge("D", "B")
    print("Test 7 graph:", g7.display())
    print("Has cycle:", has_cycle_directed(g7), "(expected: True)")


if __name__ == "__main__":
    run_tests()