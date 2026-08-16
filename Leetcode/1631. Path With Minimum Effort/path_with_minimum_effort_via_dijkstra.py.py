from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
            row_len, col_len = len(heights), len(heights[0])
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            distances = [[float('inf')] * col_len for _ in range(row_len)]
            heap = [(0,0,0)]
            distances[0][0] = 0
            while heap:
                prev_max_height, x,y = heappop(heap)
                if x==row_len-1 and y == col_len-1:
                    return prev_max_height
                if prev_max_height > distances[x][y]:
                    continue
                for i, j in directions:
                    new_i, new_j = x+i, y+j
                    if new_i>=0 and new_i < row_len and new_j >=0 and new_j < col_len:
                        current_diff = abs(heights[x][y] - heights[new_i][new_j])
                        max_val = max(prev_max_height, current_diff)
                        if max_val < distances[new_i][new_j]:
                            distances[new_i][new_j] = max_val
                            heappush(heap,(max_val, new_i, new_j))
            return distances[(row_len-1, col_len-1)]
    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        graph={}
        row_len, col_len = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        distances = {}
        for i in range(row_len):
            for j in range(col_len):
                childs = {}
                val = heights[i][j]
                for x,y in directions:
                    new_i, new_j = i+x, j+y
                    if new_i >=0 and new_i < row_len and new_j >=0 and new_j < col_len:
                        diff = abs(val-heights[new_i][new_j])
                        childs[(new_i,new_j)] = diff
                graph[(i,j)] = childs
                distances[(i,j)] = float('inf')
        heap = [(0, (0,0))]
        distances[(0,0)] = 0
        while heap:
            height, item = heappop(heap)
            x,y = item
            for key, val in graph[(x,y)].items():
                max_val = max(height, val)
                if max_val < distances[key]:
                    distances[key] = max_val
                    heappush(heap,(max_val, key))
        return distances[(row_len-1, col_len-1)]

        

sol = Solution()
print(sol.minimumEffortPath([[1,10,6,7,9,10,4,9]]))
print(sol.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(sol.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(sol.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
print(sol.minimumEffortPath([[3]]))
print(sol.minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]))
print(sol.minimumEffortPath([[10,8],[10,8],[1,2],[10,3],[1,3],[6,3],[5,2]]))
print(sol.minimumEffortPath([[8,3,2,5,2,10,7,1,8,9],[1,4,9,1,10,2,4,10,3,5],[4,10,10,3,6,1,3,9,8,8],[4,4,6,10,10,10,2,10,8,8],[9,10,2,4,1,2,2,6,5,7],[2,9,2,6,1,4,7,6,10,9],[8,8,2,10,8,2,3,9,5,3],[2,10,9,3,5,1,7,4,5,6],[2,3,9,2,5,10,2,7,1,8],[9,10,4,10,7,4,9,3,1,6]]))