from typing import List

class UnionFind():
    
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
        
    def find(self, u):
        root = u
        while root != self.parent[root]:
            root = self.parent[root]
        #path compression
        start = u
        while start != root:
            child_parent = self.parent[start]
            self.parent[start] = root
            start = child_parent
        return root
    
    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u==parent_v:
            return False
        if self.rank[parent_u]>self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        elif self.rank[parent_v]>self.rank[parent_u]:
            self.parent[parent_u] = parent_v
        else: 
            self.parent[parent_v] = parent_u
            self.rank[parent_u] +=1
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union_find = UnionFind(n)
        ans = None
        for edge in edges:
            u,v = edge
            if not union_find.union(u,v):
                ans = edge
        return ans
    
    
sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))