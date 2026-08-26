from typing import List
from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        m = len(edges)
        graph = [[] for _ in range(n)]
        in_degree = [0]*n
        for u,v in edges:
            graph[u].append(v)
            in_degree[v] +=1

        queue = deque([i for i in range(n) if in_degree[i]==0])
        dp = [[0] * 26 for _ in range(n)]

        # intial values in respective arrays
        for i in range(n):
            dp[i][ord(colors[i])-ord('a')] = 1

        total_node_accessed = 0
        max_color_val = 0

        while queue:
            u = queue.popleft()
            total_node_accessed +=1 

            max_color_val = max(max_color_val, max(dp[u]))
            for neighbour in graph[u]:
                v_ch_index = ord(colors[neighbour])-ord('a')
                for ch in range(26):
                    dp[neighbour][ch] = max(dp[neighbour][ch],dp[u][ch]+(1 if ch==v_ch_index else 0))
                in_degree[neighbour] -=1
                if in_degree[neighbour]==0:
                    queue.append(neighbour)
        return max_color_val if total_node_accessed==n else -1
            

sol = Solution()
print(sol.largestPathValue("abaca",[[0,1],[0,2],[2,3],[3,4]]))
print(sol.largestPathValue("a", [[0,0]]))