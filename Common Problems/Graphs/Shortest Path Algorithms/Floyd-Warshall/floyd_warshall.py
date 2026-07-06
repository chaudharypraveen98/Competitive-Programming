"""
Floyd-Warshall skeleton — just fill in the floyd_warshall() function below.

Reminder of the idea:
- Computes shortest distances between EVERY pair of vertices (all-pairs), not just from one start.
- dist[i][j] = shortest distance from i to j.
- Core idea: for every possible "intermediate" vertex k, check if going i -> k -> j
  is shorter than the current known i -> j. If so, update it.
- Three nested loops: outer loop is the intermediate vertex k, inner two loops are i, j.
  IMPORTANT: k must be the OUTERMOST loop -- this is the most common mistake.

Handles negative edge weights (but not negative cycles).
Works on a matrix representation since the algorithm is defined in terms of dist[i][j].
"""

INF = float('inf')


class MatrixGraph:
    def __init__(self, directed=False):
        self.directed = directed
        self.vertices = []
        self.index = {}
        self.matrix = []

    def add_vertex(self, v):
        if v in self.index:
            return False
        self.index[v] = len(self.vertices)
        self.vertices.append(v)
        for row in self.matrix:
            row.append(INF)
        self.matrix.append([INF] * len(self.vertices))
        self.matrix[-1][-1] = 0   # distance from a vertex to itself is 0
        return True

    def add_edge(self, u, v, weight):
        if u not in self.index:
            self.add_vertex(u)
        if v not in self.index:
            self.add_vertex(v)
        i, j = self.index[u], self.index[v]
        self.matrix[i][j] = weight
        if not self.directed:
            self.matrix[j][i] = weight
        return True

    def display(self):
        return {
            self.vertices[i]: {
                self.vertices[j]: self.matrix[i][j]
                for j in range(len(self.vertices))
            }
            for i in range(len(self.vertices))
        }


# ---------------------------------------------------------
# YOUR CODE HERE
# ---------------------------------------------------------

def floyd_warshall(graph):
    """
    Return a dict of dicts: result[u][v] = shortest distance from u to v.
    Unreachable pairs should map to float('inf').
    Distance from any vertex to itself should be 0.

    Hint: start by copying graph.matrix into a new distance matrix,
    then run the triple nested loop (k, i, j -- in that order).
    Convert back to vertex-name dict of dicts before returning.
    """
    rows  = len(graph.matrix)
    distances = [list(row) for row in graph.matrix]
    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                distances[i][j] = min(distances[i][j],distances[i][k]+distances[k][j])
    results = {
        graph.vertices[i]:{
            graph.vertices[j]:distances[i][j] for j in range(rows)
        } for i in range(rows)
    }
    return results


# ---------------------------------------------------------
# TEST CASES — do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    # Test 1: simple directed graph, verify a shorter path through an intermediate node is found
    #     A -3-> B -1-> C
    #     A ----------10---> C   (direct edge, but longer than going through B)
    g1 = MatrixGraph(directed=True)
    g1.add_edge("A", "B", 3)
    g1.add_edge("B", "C", 1)
    g1.add_edge("A", "C", 10)

    print("Test 1 graph:", g1.display())
    result1 = floyd_warshall(g1)
    print("All-pairs shortest paths:", result1)
    # expected: A->C should be 4 (via B), not 10 (direct edge)
    # expected result1['A']['C'] == 4
    print()

    # Test 2: undirected graph
    #     A --2-- B --2-- C
    #     A ------5------ C   (direct edge, longer than via B)
    g2 = MatrixGraph(directed=False)
    g2.add_edge("A", "B", 2)
    g2.add_edge("B", "C", 2)
    g2.add_edge("A", "C", 5)

    print("Test 2 graph:", g2.display())
    result2 = floyd_warshall(g2)
    print("All-pairs shortest paths:", result2)
    # expected result2['A']['C'] == 4  (A->B->C = 2+2=4, cheaper than direct 5)
    print()

    # Test 3: disconnected graph (some pairs unreachable)
    #     A -1-> B         C -1-> D   (separate components)
    g3 = MatrixGraph(directed=True)
    g3.add_edge("A", "B", 1)
    g3.add_edge("C", "D", 1)

    print("Test 3 graph:", g3.display())
    result3 = floyd_warshall(g3)
    print("All-pairs shortest paths:", result3)
    # expected result3['A']['C'] == inf and result3['A']['D'] == inf
    print()

    # Test 4: single node, no edges
    g4 = MatrixGraph(directed=False)
    g4.add_vertex("X")

    print("Test 4 graph:", g4.display())
    result4 = floyd_warshall(g4)
    print("All-pairs shortest paths:", result4)
    # expected: {'X': {'X': 0}}
    print()

    # Test 5: negative edge weight (no negative cycle) -- Floyd-Warshall should still work
    #     A -4-> B -(-2)-> C
    g5 = MatrixGraph(directed=True)
    g5.add_edge("A", "B", 4)
    g5.add_edge("B", "C", -2)

    print("Test 5 graph:", g5.display())
    result5 = floyd_warshall(g5)
    print("All-pairs shortest paths:", result5)
    # expected result5['A']['C'] == 2  (4 + (-2))
    print()

    # Test 6: verify self-distance is always 0, even with cycles
    #     A -1-> B -1-> C -1-> A   (cycle)
    g6 = MatrixGraph(directed=True)
    g6.add_edge("A", "B", 1)
    g6.add_edge("B", "C", 1)
    g6.add_edge("C", "A", 1)

    print("Test 6 graph:", g6.display())
    result6 = floyd_warshall(g6)
    print("All-pairs shortest paths:", result6)
    # expected result6['A']['A'] == 0, result6['B']['B'] == 0, result6['C']['C'] == 0
    # expected result6['A']['C'] == 2  (A->B->C)


if __name__ == "__main__":
    run_tests()