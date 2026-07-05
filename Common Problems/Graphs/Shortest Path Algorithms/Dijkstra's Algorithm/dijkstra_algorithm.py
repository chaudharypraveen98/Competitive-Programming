"""
Dijkstra's Algorithm skeleton — just fill in the dijkstra() function below.

Reminder of the idea:
- Maintain a running "best known distance" to every node (start = 0, everything else = infinity).
- Always expand the closest not-yet-finalized node next (use a min-heap for this).
- When you visit a node's neighbor, see if going through the current node gives
  a shorter distance than what's currently recorded — if so, update it ("relax the edge").
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


# ---------------------------------------------------------
# YOUR CODE HERE
# ---------------------------------------------------------

def dijkstra(graph, start):
    """
    Return a dict mapping every reachable vertex -> shortest distance from `start`.
    Unreachable vertices map to float('inf').
    """
    # Step 1: initialize all distances to infinity, except start = 0
    distances = {vertex: float('inf') for vertex in graph.adjacent_list}
    distances[start] = 0

    # Step 2: min-heap of (distance, node) -- always pop the closest unprocessed node
    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)

        # Stale entry check: if we've already found a shorter path to this node
        # since this entry was pushed, skip it.
        if current_dist > distances[node]:
            continue

        for neighbor, weight in graph.adjacent_list[node].items():
            distance_through_node = current_dist + weight

            # Relaxation step: is going through `node` better than what we had?
            if distance_through_node < distances[neighbor]:
                distances[neighbor] = distance_through_node
                heapq.heappush(heap, (distance_through_node, neighbor))

    return distances


# ---------------------------------------------------------
# TEST CASES — do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    # Test 1: simple weighted undirected graph
    #        A --1-- B
    #        |        \
    #        4         2
    #        |          \
    #        C --1------ D
    g1 = WeightedGraph(directed=False)
    g1.add_edge("A", "B", 1)
    g1.add_edge("A", "C", 4)
    g1.add_edge("B", "D", 2)
    g1.add_edge("C", "D", 1)

    print("Test 1 graph:", g1.display())
    print("Dijkstra from A:", dijkstra(g1, "A"))
    # expected: {'A': 0, 'B': 1, 'C': 4, 'D': 3}
    # (A->B->D = 1+2=3, cheaper than A->C->D = 4+1=5)
    print()

    # Test 2: directed graph, only one path exists
    #     A -5-> B -3-> C
    g2 = WeightedGraph(directed=True)
    g2.add_edge("A", "B", 5)
    g2.add_edge("B", "C", 3)

    print("Test 2 graph:", g2.display())
    print("Dijkstra from A:", dijkstra(g2, "A"))
    # expected: {'A': 0, 'B': 5, 'C': 8}
    print()

    # Test 3: disconnected graph (some nodes unreachable)
    #     A -1-> B         C -1-> D   (separate components)
    g3 = WeightedGraph(directed=True)
    g3.add_edge("A", "B", 1)
    g3.add_edge("C", "D", 1)

    print("Test 3 graph:", g3.display())
    print("Dijkstra from A:", dijkstra(g3, "A"))
    # expected: {'A': 0, 'B': 1, 'C': inf, 'D': inf}
    print()

    # Test 4: single node, no edges
    g4 = WeightedGraph(directed=False)
    g4.add_vertex("X")

    print("Test 4 graph:", g4.display())
    print("Dijkstra from X:", dijkstra(g4, "X"))
    # expected: {'X': 0}
    print()

    # Test 5: multiple paths, must pick the cheapest one (classic trap for BFS-only thinkers)
    #     A -1-> B -1-> C -1-> D      (total cost 3, but more hops)
    #     A ----------10-------> D    (direct edge, fewer hops but expensive)
    g5 = WeightedGraph(directed=True)
    g5.add_edge("A", "B", 1)
    g5.add_edge("B", "C", 1)
    g5.add_edge("C", "D", 1)
    g5.add_edge("A", "D", 10)

    print("Test 5 graph:", g5.display())
    print("Dijkstra from A:", dijkstra(g5, "A"))
    # expected: {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    # (must NOT pick the direct A->D edge of weight 10 -- fewer hops isn't the same as shortest distance)


if __name__ == "__main__":
    run_tests()