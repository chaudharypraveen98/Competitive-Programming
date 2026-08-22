from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        total = 0
        visited =set()
        
        def dfs(city):
            visited.add(city)
            for neigbhour in range(n):
                if neigbhour not in visited and isConnected[city][neigbhour]:
                    dfs(neigbhour)
            
        for i in range(n):
            if i not in visited:
                total+=1
                dfs(i)
        return total

sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
# print(sol.findCircleNum())
