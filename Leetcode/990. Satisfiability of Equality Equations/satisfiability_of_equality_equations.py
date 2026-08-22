from typing import List

class UnionFind:
    def __init__(self):
        # 26 lowercase English letters
        self.parent = {chr(i):chr(i) for i in range(ord('a'), ord('z')+1)}
        self.rank = {chr(i):0 for i in range(ord('a'), ord('z')+1)}

    def find(self, u: str) -> str:
        root = u
        while root != self.parent[root]:
            root = self.parent[root]
        curr = u
        while curr != root:
            self.parent[curr], curr = root, self.parent[curr]
        return root

    def union(self, u: str, v: str) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        # Step 1: Union all equality constraints
        for eq in equations:
            if eq[1:3] == "==":
                uf.union(eq[0], eq[3])

        # Step 2: Validate against inequality constraints
        for eq in equations:
            if eq[1:3] == "!=":
                if uf.find(eq[0]) == uf.find(eq[3]):
                    return False

        return True


sol = Solution()
print(sol.equationsPossible(["a==b","b!=a"]))
print(sol.equationsPossible(["b==a","a==b"]))
