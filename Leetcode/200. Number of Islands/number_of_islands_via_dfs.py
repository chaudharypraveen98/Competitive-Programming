class Solution:
    def __init__(self):
        self.direction = [(1,0), (-1,0), (0,-1),(0,1)]
    def graph_from_node_via_dfs(self,graph, row, col, visited):
        if row < 0 or col < 0 or row >= len(graph) or col >= len(graph[0]):
            return 0
        if (row,col) in visited:
            return 0
        visited.add((row,col))
        if graph[row][col]=='0':
            return 0
        for i,j in self.direction:
            self.graph_from_node_via_dfs(graph,row+i,col+j, visited)
        return 1
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited =set()
        total = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    total += self.graph_from_node_via_dfs(grid, i,j, visited)
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