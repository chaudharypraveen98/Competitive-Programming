from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,-1),(0,1)]
        def bfs(start, count = 0):
            queue = deque([start])
            while queue:
                items = queue.popleft()
                temp_res = []
                for item in items: 
                    new_row, new_col = item
                    
                    for x,y in directions:
                        nr = new_row+x
                        nc = new_col+y
                        if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc] != 0:
                            visited[nr][nc] = True
                            temp_res.append((nr,nc))
                if temp_res:
                    count  += 1
                    queue.append(temp_res)
            return count
        
        start_nodes = []   
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    visited[i][j] = True
                    start_nodes.append((i,j))
        steps = bfs(start_nodes, 0)        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]==1:
                    return -1
        return steps

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(sol.orangesRotting([[0,2]]))
print(sol.orangesRotting([[0]]))
print(sol.orangesRotting([[0,2,2]]))