"""
Kruskal's Algorithm (MST) skeleton -- fill in UnionFind methods first, then kruskal().

------------------------------------------------------------
Union-Find (Disjoint Set Union) -- the building block
------------------------------------------------------------
Tracks which "group" each vertex belongs to, supporting two operations:
- find(x): returns a representative ID for x's current group
- union(x, y): merges x's group and y's group into one

Two optimizations (both included as hints below):
- Path compression (in find): when finding x's root, point every node
  along the way DIRECTLY to the root, so future lookups are faster.
- Union by rank: when merging two groups, attach the smaller tree under
  the bigger one's root, to keep tree depth low.

------------------------------------------------------------
Kruskal's Algorithm -- the MST builder
------------------------------------------------------------
1. Sort all edges by weight, ascending.
2. Go through edges in that order. For each edge (u, v, w):
   - If find(u) != find(v): they're in different groups, so adding this
     edge won't create a cycle. Add it to the MST, and union(u, v).
   - If find(u) == find(v): adding this edge WOULD create a cycle. Skip it.
3. Stop once you've added (V - 1) edges (a spanning tree needs exactly that many).
"""


class UnionFind:
    def __init__(self, vertices):
        # each vertex starts as its own parent (its own group)
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        """
        Return the representative (root) of x's group.
        Hint: if self.parent[x] != x, recurse upward, and while you're at it,
        set self.parent[x] directly to the root you find (path compression).
        """
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x, y):
        """
        Merge the groups containing x and y.
        Return True if they were in different groups (merge happened),
        False if they were already in the same group (would create a cycle).
        Hint: use self.rank to decide which root becomes the parent of the other.
        """
        parent_of_x = self.find(x)
        parent_of_y = self.find(y)
        if parent_of_x == parent_of_y:
            return False
        if self.rank[parent_of_x] > self.rank[parent_of_y]:
            self.parent[parent_of_y] = parent_of_x
        elif self.rank[parent_of_y] > self.rank[parent_of_x]:
            self.parent[parent_of_x] = parent_of_y
        else:
            self.rank[parent_of_x] +=1
            self.parent[parent_of_y] = parent_of_x
        return True


# ---------------------------------------------------------
# YOUR CODE HERE
# ---------------------------------------------------------

def kruskal(vertices, edges):
    """
    vertices: list of vertex names, e.g. ['A', 'B', 'C']
    edges: list of (u, v, weight) tuples

    Return (total_weight, mst_edges) where mst_edges is the list of
    (u, v, weight) tuples included in the minimum spanning tree.

    If the graph is disconnected (no spanning tree covering all vertices
    is possible), return whatever MST forest was still built along with
    its total weight -- just build as much as the edges allow.
    """
    sorted_edges = sorted(edges,key=lambda x:x[2])
    res = []
    total_weight = 0
    union_find = UnionFind(vertices)
    for i in sorted_edges:
        if len(res) == len(vertices)-1:
            break
        x,y,w = i
        if union_find.union(x,y):
            total_weight += w
            res.append(i)

    return total_weight, res


# ---------------------------------------------------------
# TEST CASES -- do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    # Test 1: simple square with a diagonal shortcut
    #     A --1-- B
    #     |       |
    #     4       2
    #     |       |
    #     C --1-- D
    #     A --5-- D  (extra, more expensive alt path)
    vertices1 = ['A', 'B', 'C', 'D']
    edges1 = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'D', 2),
        ('C', 'D', 1),
        ('A', 'D', 5),
    ]
    weight1, mst1 = kruskal(vertices1, edges1)
    print("Test 1 edges:", edges1)
    print("MST:", mst1, "Total weight:", weight1)
    print("Expected total weight: 4  (edges A-B:1, C-D:1, B-D:2 -- skip A-C:4 and A-D:5, cycle/expensive)")
    print()

    # Test 2: already a tree (no cycles possible, every edge must be used)
    #     A -1- B -2- C -3- D
    vertices2 = ['A', 'B', 'C', 'D']
    edges2 = [
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('C', 'D', 3),
    ]
    weight2, mst2 = kruskal(vertices2, edges2)
    print("Test 2 edges:", edges2)
    print("MST:", mst2, "Total weight:", weight2)
    print("Expected total weight: 6  (all 3 edges required, no cycles to skip)")
    print()

    # Test 3: triangle -- must skip the most expensive edge to avoid a cycle
    #     A -1- B -1- C -1- A
    vertices3 = ['A', 'B', 'C']
    edges3 = [
        ('A', 'B', 1),
        ('B', 'C', 1),
        ('C', 'A', 1),
    ]
    weight3, mst3 = kruskal(vertices3, edges3)
    print("Test 3 edges:", edges3)
    print("MST:", mst3, "Total weight:", weight3)
    print("Expected total weight: 2  (any 2 of the 3 edges -- all equal weight, so multiple valid MSTs)")
    print()

    # Test 4: single vertex, no edges
    vertices4 = ['X']
    edges4 = []
    weight4, mst4 = kruskal(vertices4, edges4)
    print("Test 4 edges:", edges4)
    print("MST:", mst4, "Total weight:", weight4)
    print("Expected total weight: 0, no edges needed for a single node")
    print()

    # Test 5: disconnected graph -- no single spanning tree possible
    #     A -1- B          C -1- D   (two separate components)
    vertices5 = ['A', 'B', 'C', 'D']
    edges5 = [
        ('A', 'B', 1),
        ('C', 'D', 1),
    ]
    weight5, mst5 = kruskal(vertices5, edges5)
    print("Test 5 edges:", edges5)
    print("MST:", mst5, "Total weight:", weight5)
    print("Expected: builds a forest -- both edges used (2 total), but graph stays disconnected overall")
    print()

    # Test 6: larger graph, multiple valid MSTs but same total weight
    #        A --2-- B
    #        |  \    |
    #        6   3   1
    #        |    \  |
    #        C --4-- D
    vertices6 = ['A', 'B', 'C', 'D']
    edges6 = [
        ('A', 'B', 2),
        ('A', 'D', 3),
        ('A', 'C', 6),
        ('B', 'D', 1),
        ('C', 'D', 4),
    ]
    weight6, mst6 = kruskal(vertices6, edges6)
    print("Test 6 edges:", edges6)
    print("MST:", mst6, "Total weight:", weight6)
    print("Expected total weight: 7  (edges B-D:1, A-B:2, C-D:4)")


if __name__ == "__main__":
    run_tests()