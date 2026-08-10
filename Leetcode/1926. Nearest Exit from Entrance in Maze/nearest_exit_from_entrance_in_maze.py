from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(-1,0), (1, 0),(0,1),(0,-1)]
        start_x, start_y = entrance
        m, n = len(maze), len(maze[0])
        queue = deque([(start_x, start_y, 0)])
        visited = {(start_x, start_y)}
        while queue:
            x,y,cost  = queue.popleft()
            if (x==0 or x == m-1 or y==0 or y==n-1) and (x, y) != (start_x, start_y):
                return cost
                
            for nr, nc in directions:
                add_x, add_y = nr+x, nc+y
                if (add_x, add_y) not in visited  and add_x>=0 and add_x<m and add_y>=0 and add_y<n and maze[add_x][add_y]!='+':
                    visited.add((nr+x, nc+y))
                    queue.append((nr+x, nc+y, cost+1))
        return -1
            
sol = Solution()
print(sol.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))
print(sol.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))
print(sol.nearestExit([[".","+"]], [0,0]))