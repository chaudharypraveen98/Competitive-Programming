"""
Prim's Algorithm -- REFERENCE SOLUTION (styled to match Kruskal's conventions)

Same logic as before, just using (u, v, weight) tuple ordering throughout,
to match WeightedGraph.add_edge(u, v, weight) and Kruskal's edge format --
makes it easier to directly compare MST outputs between the two algorithms.
"""

import heapq


class WeightedGraph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacent_list = {}   # vertex -> {neighbor: weight}

    def add_vertex(self, v):
        if v not in self.adjacent_list:
            self.adjacent_list[v] = {}

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacent_list[u][v] = weight
        if not self.directed:
            self.adjacent_list[v][u] = weight

    def display(self):
        return self.adjacent_list


def prim(graph, start):
    """
    Return (total_weight, mst_edges) for the graph's minimum spanning tree,
    starting the tree-growing process from `start`.

    mst_edges is a list of (u, v, weight) tuples, matching the same
    (u, v, weight) convention used by WeightedGraph.add_edge and Kruskal's.

    If the graph is disconnected, returns the MST for the reachable
    portion only.
    """
    heap = []               # min-heap of (weight, u, v) candidate edges
    visited = {start}
    mst_edges = []
    total_weight = 0

    def push_edges_from(vertex):
        for neighbor, weight in graph.adjacent_list[vertex].items():
            heapq.heappush(heap, (weight, vertex, neighbor))

    push_edges_from(start)

    while heap:
        weight, u, v = heapq.heappop(heap)

        if v in visited:
            continue   # stale edge -- v already joined the tree via a cheaper path

        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight
        push_edges_from(v)

    return total_weight, mst_edges


# ---------------------------------------------------------
# TEST CASES
# ---------------------------------------------------------

def run_tests():
    g1 = WeightedGraph(directed=False)
    g1.add_edge("A", "B", 1)
    g1.add_edge("A", "C", 4)
    g1.add_edge("B", "D", 2)
    g1.add_edge("C", "D", 1)
    g1.add_edge("A", "D", 5)
    print("Test 1:", prim(g1, "A"), "-- expected weight 4")

    g2 = WeightedGraph(directed=False)
    g2.add_edge("A", "B", 1)
    g2.add_edge("B", "C", 2)
    g2.add_edge("C", "D", 3)
    print("Test 2:", prim(g2, "A"), "-- expected weight 6")

    g3 = WeightedGraph(directed=False)
    g3.add_edge("A", "B", 1)
    g3.add_edge("B", "C", 1)
    g3.add_edge("C", "A", 1)
    print("Test 3:", prim(g3, "A"), "-- expected weight 2")

    g4 = WeightedGraph(directed=False)
    g4.add_vertex("X")
    print("Test 4:", prim(g4, "X"), "-- expected weight 0")

    g5 = WeightedGraph(directed=False)
    g5.add_edge("A", "B", 1)
    g5.add_edge("C", "D", 1)
    print("Test 5:", prim(g5, "A"), "-- expected weight 1 (only A-B reachable)")

    g6 = WeightedGraph(directed=False)
    g6.add_edge("A", "B", 2)
    g6.add_edge("A", "D", 3)
    g6.add_edge("A", "C", 6)
    g6.add_edge("B", "D", 1)
    g6.add_edge("C", "D", 4)
    print("Test 6:", prim(g6, "A"), "-- expected weight 7 (matches Kruskal's)")


if __name__ == "__main__":
    run_tests()