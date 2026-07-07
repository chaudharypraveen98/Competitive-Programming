"""
Bellman-Ford skeleton — just fill in the bellman_ford() function below.

Reminder of the idea:
- Like Dijkstra, computes shortest distance from ONE start node to every other node.
- Unlike Dijkstra, it does NOT greedily pick "closest node first" -- instead it just
  relaxes EVERY edge, and repeats this V-1 times (V = number of vertices).
- Why V-1 times? The longest possible shortest path (with no cycles) uses at most
  V-1 edges, so after V-1 full rounds of relaxing every edge, all distances are guaranteed final.
- Bonus: run ONE more round (the V-th). If any distance still improves, there's a
  negative-weight cycle reachable from start -- shortest path isn't well-defined.

Works correctly with negative edge weights (unlike Dijkstra).
Needs an EDGE LIST, not an adjacency list/matrix -- since you relax every edge directly.
"""

INF = float('inf')


class EdgeListGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = []   # list of (u, v, weight) tuples

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.edges.append((u, v, weight))

    def display(self):
        return {"vertices": sorted(self.vertices), "edges": self.edges}


# ---------------------------------------------------------
# YOUR CODE HERE
# ---------------------------------------------------------

def bellman_ford(graph, start):
    """
    Return a dict mapping every reachable vertex -> shortest distance from `start`.
    Unreachable vertices should map to float('inf').

    Raise a ValueError("Negative weight cycle detected") if one exists
    that is reachable from `start`.

    Hint:
    - Initialize distances (start = 0, everything else = inf).
    - Repeat (V - 1) times: for every edge (u, v, w), if dist[u] + w < dist[v], update dist[v].
    - Then do ONE more pass: if anything still improves, raise the ValueError.
    """
    distances  = {node:float('inf') for node in graph.vertices}
    distances[start] = 0

    for _ in range(len(graph.vertices)-1):
        for u, v, weight in graph.edges:
            if distances[u] != float('inf') and distances[u]+weight < distances[v]:
                distances[v] = distances[u]+weight
    
    for u, v, weight in graph.edges:
        if distances[u] != float('inf') and distances[u]+weight < distances[v]:
            raise ValueError("Negative weight cycle detected")
    return distances


# ---------------------------------------------------------
# TEST CASES — do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    # Test 1: simple graph, no negative edges (sanity check vs Dijkstra-style result)
    #     A -1-> B -1-> C -1-> D
    #     A ----------10------> D
    g1 = EdgeListGraph()
    g1.add_edge("A", "B", 1)
    g1.add_edge("B", "C", 1)
    g1.add_edge("C", "D", 1)
    g1.add_edge("A", "D", 10)

    print("Test 1 graph:", g1.display())
    print("Bellman-Ford from A:", bellman_ford(g1, "A"))
    # expected: {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    print()

    # Test 2: negative edge weight, no negative cycle
    #     A -4-> B -(-2)-> C
    g2 = EdgeListGraph()
    g2.add_edge("A", "B", 4)
    g2.add_edge("B", "C", -2)

    print("Test 2 graph:", g2.display())
    print("Bellman-Ford from A:", bellman_ford(g2, "A"))
    # expected: {'A': 0, 'B': 4, 'C': 2}
    print()

    # Test 3: disconnected graph (some nodes unreachable)
    #     A -1-> B         C -1-> D   (separate components)
    g3 = EdgeListGraph()
    g3.add_edge("A", "B", 1)
    g3.add_edge("C", "D", 1)

    print("Test 3 graph:", g3.display())
    print("Bellman-Ford from A:", bellman_ford(g3, "A"))
    # expected: {'A': 0, 'B': 1, 'C': inf, 'D': inf}
    print()

    # Test 4: single node, no edges
    g4 = EdgeListGraph()
    g4.add_vertex("X")

    print("Test 4 graph:", g4.display())
    print("Bellman-Ford from X:", bellman_ford(g4, "X"))
    # expected: {'X': 0}
    print()

    # Test 5: negative cycle reachable from start -- should raise ValueError
    #     A -1-> B -1-> C -(-5)-> B   (B -> C -> B loses 4 each loop)
    g5 = EdgeListGraph()
    g5.add_edge("A", "B", 1)
    g5.add_edge("B", "C", 1)
    g5.add_edge("C", "B", -5)

    print("Test 5 graph:", g5.display())
    try:
        print("Bellman-Ford from A:", bellman_ford(g5, "A"))
        print("ERROR: expected a ValueError to be raised, but none was!")
    except ValueError as e:
        print("Correctly raised ValueError:", e)
    print()

    # Test 6: negative cycle exists, but NOT reachable from start -- should NOT raise
    #     A -1-> B          (separate) X -1-> Y -(-5)-> X   (negative cycle, unrelated component)
    g6 = EdgeListGraph()
    g6.add_edge("A", "B", 1)
    g6.add_edge("X", "Y", 1)
    g6.add_edge("Y", "X", -5)

    print("Test 6 graph:", g6.display())
    print("Bellman-Ford from A:", bellman_ford(g6, "A"))
    # expected: {'A': 0, 'B': 1, 'X': inf, 'Y': inf}  -- no error, cycle is unreachable from A


if __name__ == "__main__":
    run_tests()