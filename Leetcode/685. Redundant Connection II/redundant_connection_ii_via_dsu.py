from typing import List, Optional, Tuple

class UnionFind():
    
    def __init__(self,n):
        self.parent = {v:v for v in range(n+1)}
        self.rank = {v:0 for v in range(n+1)}

    def find(self, u):
        root = u
        while root != self.parent[root]:
            root = self.parent[root]
            
        start = u
        while start != root:
            child_parent = self.parent[start]
            self.parent[start] = root
            start = child_parent
        return root
    
    def union(self, u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u==parent_v:
            return False
        if self.rank[parent_u]>self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        elif self.rank[parent_v]> self.rank[parent_u]:
            self.parent[parent_u] = parent_v
        else:
            self.rank[parent_u] +=1
            self.parent[parent_v] = parent_u
        return True
            

class Solution:
    def findRedundantDirectedConnection(
      self, edges: List[List[int]]
  ) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        indegree_node = None
        for u,v in edges:
            indegree[v] +=1
        
        for node in range(len(indegree)):
            if indegree[node]==2:
                indegree_node = node
                break
        if indegree_node:
            two_nodes = []
            for u,v in edges:
                if indegree_node==v:
                    two_nodes.append([u,v])
            cand1, cand2 = two_nodes[0], two_nodes[1]
            dsu = UnionFind(n)
            for edge in edges:
                u,v = edge
                if cand2 and cand2==edge:
                    continue
                if not dsu.union(u,v):
                    return cand1
            return cand2
        else:
            dsu = UnionFind(n)
            for u,v in edges:
                if not dsu.union(u,v):
                    return [u,v]

        return []

sol = Solution()
print(sol.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))
print(sol.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))
print(sol.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])) #[2,1]
print(sol.findRedundantDirectedConnection([[5,2],[5,1],[3,1],[3,4],[3,5]]))