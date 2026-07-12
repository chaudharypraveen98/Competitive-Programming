"""
Union-Find (Disjoint Set Union / DSU) skeleton -- fill in find() and union() below.

Tracks which "group" (connected component) each element belongs to, supporting:
- find(x): returns a representative ID for x's current group (the "root")
- union(x, y): merges x's group and y's group into one

Two classic optimizations, both expected here:

1. PATH COMPRESSION (in find):
   When finding x's root, every node visited along the way should be
   re-pointed DIRECTLY to the root -- so future find() calls on those
   nodes are instant. Without this, chains of unions can degrade to O(n)
   per find() in the worst case.

2. UNION BY RANK (in union):
   When merging two groups, attach the SMALLER tree under the bigger
   tree's root (rank = rough estimate of tree height). Without this,
   naive unions can build long chains, again degrading find() to O(n).

With BOTH optimizations, find/union become nearly O(1) each --
technically O(alpha(n)), where alpha is the inverse Ackermann function,
which is so slow-growing it's effectively constant for any realistic input.
"""


class UnionFind:
    def __init__(self, elements):
        # each element starts as its own parent (its own group of size 1)
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}

    def find(self, x):
        """
        Return the root/representative of x's group.
        Hint: if self.parent[x] != x, x isn't the root -- recurse/loop upward,
        and set self.parent[x] directly to the root as you go (path compression).
        """
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x]!=root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x, y):
        """
        Merge the groups containing x and y.
        Return True if a merge actually happened (they were in different groups).
        Return False if x and y were already in the same group (no-op --
        this is your cycle-detection signal in algorithms like Kruskal's).
        Hint: find both roots first. If they're already equal, return False.
        Otherwise, attach the lower-rank root under the higher-rank root
        (if ranks are equal, pick either and increment its rank).
        """
        parent_of_x = self.find(x)
        parent_of_y = self.find(y)
        if parent_of_x==parent_of_y:
            return False
        if self.rank[parent_of_x] > self.rank[parent_of_y]:
            self.parent[parent_of_y] = parent_of_x
        elif self.rank[parent_of_x] < self.rank[parent_of_y]:
            self.parent[parent_of_x] = parent_of_y
        else:
            self.parent[parent_of_y] = parent_of_x
            self.rank[parent_of_x] += 1   # only bump rank on a genuine tie
        return True

    def connected(self, x, y):
        """Convenience method: are x and y in the same group?"""
        return self.find(x) == self.find(y)


# ---------------------------------------------------------
# TEST CASES -- do not need to modify below this line
# ---------------------------------------------------------

def run_tests():
    print("===== Test 1: basic union + connected =====")
    uf = UnionFind(['A', 'B', 'C', 'D', 'E'])
    print("Initially, A and B connected?", uf.connected('A', 'B'), "(expected: False)")
    uf.union('A', 'B')
    print("After union(A, B), connected?", uf.connected('A', 'B'), "(expected: True)")
    print("C and D connected?", uf.connected('C', 'D'), "(expected: False)")
    print()

    print("===== Test 2: transitive connectivity =====")
    uf2 = UnionFind(['A', 'B', 'C', 'D'])
    uf2.union('A', 'B')
    uf2.union('B', 'C')
    print("A and C connected (via B)?", uf2.connected('A', 'C'), "(expected: True)")
    print("A and D connected?", uf2.connected('A', 'D'), "(expected: False)")
    print()

    print("===== Test 3: union returns False on redundant union (cycle signal) =====")
    uf3 = UnionFind(['A', 'B', 'C'])
    print("union(A, B):", uf3.union('A', 'B'), "(expected: True, first-time merge)")
    print("union(B, C):", uf3.union('B', 'C'), "(expected: True, first-time merge)")
    print("union(A, C):", uf3.union('A', 'C'), "(expected: False -- A and C already connected via B)")
    print()

    print("===== Test 4: merging two separate groups of 2 =====")
    uf4 = UnionFind(['A', 'B', 'C', 'D'])
    uf4.union('A', 'B')
    uf4.union('C', 'D')
    print("A and C connected before merge?", uf4.connected('A', 'C'), "(expected: False)")
    uf4.union('B', 'C')
    print("A and D connected after union(B, C)?", uf4.connected('A', 'D'), "(expected: True)")
    print()

    print("===== Test 5: single element, no unions =====")
    uf5 = UnionFind(['X'])
    print("X connected to itself?", uf5.connected('X', 'X'), "(expected: True)")
    print()

    print("===== Test 6: counting distinct groups after several unions =====")
    uf6 = UnionFind(['A', 'B', 'C', 'D', 'E', 'F'])
    uf6.union('A', 'B')
    uf6.union('C', 'D')
    uf6.union('E', 'F')
    uf6.union('B', 'C')
    roots = {uf6.find(e) for e in ['A', 'B', 'C', 'D', 'E', 'F']}
    print("Number of distinct groups:", len(roots), "(expected: 2 -- {A,B,C,D} merged, {E,F} separate)")


if __name__ == "__main__":
    run_tests()