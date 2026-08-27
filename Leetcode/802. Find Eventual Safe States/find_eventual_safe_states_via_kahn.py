from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree= [0]*n
        reversed_graph =[[] for _ in range(n)]
        for u in range(n):
            out_degree[u] = len(graph[u])
            for v in graph[u]:
                reversed_graph[v].append(u)
        
        # Start with terminal nodes (out_degree == 0 in original graph)
        queue = deque([i for i in range(n) if out_degree[i]==0])
        res = []
        while queue:
            parent = queue.popleft()
            res.append(parent)
            
            # Push safety backwards to parents in the original graph
            for neighbour in reversed_graph[parent]:
                out_degree[neighbour] -=1
                
                # If all outgoing edges of parent lead to confirmed safe nodes
                if out_degree[neighbour]==0:
                    queue.append(neighbour)
        
        return [i for i in range(n) if out_degree[i]==0]


sol = Solution()
print(sol.eventualSafeNodes(
    [[1, 2], [2, 3], [5], [0], [5], [], []]))  # [2,4,5,6]
print(sol.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))  # [4]
