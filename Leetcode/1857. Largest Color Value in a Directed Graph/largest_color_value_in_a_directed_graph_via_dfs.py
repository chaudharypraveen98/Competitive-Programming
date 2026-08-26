from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        WHITE, GREY, BLACK = 0,1,2

        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)

        dp = [[0] * 26 for _ in range(n)]
        max_color_val = 0
        state = [WHITE] * n

        def dfs(node):
            state[node] = GREY

            for neigbhour in graph[node]:
                if state[neigbhour]==GREY:
                    return False
                if state[neigbhour]==WHITE:
                    if not dfs(neigbhour):
                        return False
                for ch in range(26):
                    if dp[neigbhour][ch] > dp[node][ch]:
                        dp[node][ch] = dp[neigbhour][ch]
            current_node_ch_index = ord(colors[node])-ord('a')
            dp[node][current_node_ch_index] +=1
            state[node] = BLACK
            return True

        for vertex in range(n):
            if state[vertex]==WHITE:
                if not dfs(vertex):
                    return -1
            max_color_val = max(max_color_val, max(dp[vertex]))
        return max_color_val
            

sol = Solution()
print(sol.largestPathValue("abaca",[[0,1],[0,2],[2,3],[3,4]]))
print(sol.largestPathValue("a", [[0,0]]))