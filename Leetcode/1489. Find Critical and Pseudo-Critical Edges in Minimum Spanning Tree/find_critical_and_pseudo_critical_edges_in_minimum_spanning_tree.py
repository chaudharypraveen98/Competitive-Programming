from typing import List

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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sorted_edges = []
        for idx in range(len(edges)):
            u,v,w = edges[idx]
            sorted_edges.append([w,u,v,idx])
        sorted_edges.sort(key=lambda x:x[0])
        def find_mst(ignoreIndex=-1, forceIndex=-1):
            dsu = UnionFind(n)
            total_w = 0
            edges_count = 0
            
            if forceIndex != -1:
                temp_u, temp_v, temp_w = edges[forceIndex]
                dsu.union(temp_u, temp_v)
                total_w +=temp_w
                edges_count += 1
            
            for w,u,v,idx in sorted_edges:
                if idx == ignoreIndex:
                    continue
                if dsu.union(u,v):
                    total_w +=w
                    edges_count += 1
                    if edges_count == n - 1:
                        break
            return total_w if edges_count == n - 1 else float('inf')
        
        initial_mst = find_mst()
        critical_edges = []
        pseudo_critical = []
        
        for i in range(len(edges)):
            if find_mst(ignoreIndex=i) > initial_mst:
                critical_edges.append(i)
            elif find_mst(forceIndex=i)==initial_mst:
                pseudo_critical.append(i)
                
        return [critical_edges,pseudo_critical]
                
                
sol = Solution()
print(sol.findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
print(sol.findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))