from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GREY, BLACK = 0, 1, 2
        n = len(graph)
        state = [WHITE]*n

        def dfs(node):
            if state[node]==GREY:
                return False
            if state[node]==BLACK:
                return True
            
            state[node] = GREY
            
            for neigbhour in graph[node]:
                if not dfs(neigbhour):
                    return False
                
            state[node] = BLACK
            return True

        return [i for i in range(n) if dfs(i)]


sol = Solution()
print(sol.eventualSafeNodes(
    [[1, 2], [2, 3], [5], [0], [5], [], []]))  # [2,4,5,6]
print(sol.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))  # [4]
