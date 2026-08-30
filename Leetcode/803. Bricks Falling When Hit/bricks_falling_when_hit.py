from typing import List

class UnionFind:
    def __init__(self, n: int) -> None:
        """
        Initialize DSU with parent pointers and component sizes.
        :param n: Total number of nodes (R * C cells + 1 virtual ROOF node).
        """
        self.parent = list(range(n))
        self.count = [1] * n

    def find(self, u: int) -> int:
        """
        Finds the root parent of node u with two-pass path compression.
        Time Complexity: O(alpha(N)) ~ O(1)
        """
        root = u
        while self.parent[root] != root:
            root = self.parent[root]

        # Path Compression: flatten the tree directly to the root
        start = u
        while start != root:
            parent = self.parent[start]
            self.parent[start] = root
            start = parent

        return root

    def union(self, u: int, v: int) -> bool:
        """
        Unions components containing u and v by size rank.
        Attaches the smaller component under the larger component.
        Time Complexity: O(alpha(N)) ~ O(1)
        """
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return False

        # Union by Size: attach smaller tree to larger tree
        if self.count[parent_u] > self.count[parent_v]:
            self.parent[parent_v] = parent_u
            self.count[parent_u] += self.count[parent_v]
        else:
            self.parent[parent_u] = parent_v
            self.count[parent_v] += self.count[parent_u]

        return True

    def size(self, u_index: int) -> int:
        """Returns the total number of connected nodes in the component containing u_index."""
        return self.count[self.find(u_index)]


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """
        Calculates the number of bricks that fall after each hit.
        
        Time Complexity:  O((R * C + K) * alpha(R * C)) -> Near linear time.
        Space Complexity: O(R * C) for the DSU parent and size arrays.
        """
        rows = len(grid)
        cols = len(grid[0])
        
        # 1D flattened index mapping: (r, c) -> r * cols + c + 1
        # Index 0 is reserved as the virtual "ROOF" super-node
        ROOF = 0
        union_find = UnionFind(rows * cols + 1)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def get_index(r: int, c: int) -> int:
            return r * cols + c + 1

        # ======================================================================
        # STEP 1: Apply all hits up-front using in-place decrements
        # ======================================================================
        # By decrementing (-= 1), we track duplicate hits cleanly:
        #   1 ->  0 (Intact brick broken by 1 hit)
        #   1 -> -1 (Intact brick hit 2 times)
        #   0 -> -1 (Empty cell hit)
        for i, j in hits:
            grid[i][j] -= 1

        # ======================================================================
        # STEP 2: Unionize intact bricks remaining after all hits (grid == 1)
        # ======================================================================
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    u_index = get_index(row, col)

                    # Connect top row bricks directly to the virtual ceiling
                    if row == 0:
                        union_find.union(u_index, ROOF)

                    # Scan Up and Left only (symmetric scanning covers all 4 edges once)
                    if row > 0 and grid[row - 1][col] == 1:
                        union_find.union(u_index, get_index(row - 1, col))
                    if col > 0 and grid[row][col - 1] == 1:
                        union_find.union(u_index, get_index(row, col - 1))

        # ======================================================================
        # STEP 3: Reverse-Time Simulation (Restore hits from last to first)
        # ======================================================================
        res = [0] * len(hits)

        for k in range(len(hits) - 1, -1, -1):
            i, j = hits[k]
            grid[i][j] += 1

            # Only process restoration if the cell becomes a fully intact brick (value == 1).
            # If value <= 0, it was an empty cell or hit multiple times and is still broken.
            if grid[i][j] != 1:
                continue

            # Record total stable bricks attached to ceiling BEFORE re-adding this brick
            roof_before = union_find.size(ROOF)
            k_index = get_index(i, j)

            # If restored brick is in the top row, connect it to ROOF
            if i == 0:
                union_find.union(k_index, ROOF)

            # Union restored brick with all 4 adjacent active neighbors
            for r, c in directions:
                nr, nc = r + i, c + j
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    ch_index = get_index(nr, nc)
                    union_find.union(ch_index, k_index)

            # Record total stable bricks attached to ceiling AFTER unions
            roof_after = union_find.size(ROOF)

            # Fallen bricks = newly stabilized bricks attached to ROOF minus the restored brick itself
            res[k] = max(0, roof_after - roof_before - 1)

        return res


# ==============================================================================
# VERIFICATION TRACE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Hitting (1, 0) drops the remaining row 1 bricks
    grid1 = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits1 = [[1, 0]]
    print("Test 1 Result:", sol.hitBricks(grid1, hits1))  # Expected: [2]

    # Test Case 2: Disconnected components never drop
    grid2 = [[1, 0, 0, 0], [1, 1, 0, 0]]
    hits2 = [[1, 1], [1, 0]]
    print("Test 2 Result:", sol.hitBricks(grid2, hits2))  # Expected: [0, 0]