from collections import deque

class Solution:
    def __init__(self):
        self.direction = [(1,0), (-1,0), (0,-1),(0,1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited =[[False]*n for _ in range(m)]
        total = 0
        def graph_from_node_via_bfs(row, col):
            queue=deque([(row,col)])
            visited[row][col] = True
            while queue:
                curr_row,curr_col  = queue.popleft()
                for i,j in self.direction:
                    nrow=curr_row+i
                    ncol=curr_col+j
                    if 0<=nrow<m and 0<=ncol<n and not visited[nrow][ncol] and grid[nrow][ncol]=='1':
                        visited[nrow][ncol]=True
                        queue.append((nrow,ncol))
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    graph_from_node_via_bfs(i,j)
                    total+=1
        return total
                    


sol = Solution()
print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))