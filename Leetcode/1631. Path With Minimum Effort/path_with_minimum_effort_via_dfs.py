class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        direction_keys = ["Down", "Up", 'Right', 'Left']
        row_len, col_len = len(heights), len(heights[0])
        memo = {}
        def dfs(i,j, recursion_stack, dir="Down"):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==row_len-1 and j==col_len-1:
                return 0
            recursion_stack.add((i,j))
            min_val = None
            current_val = heights[i][j]
            for item_index in range(4):
                x,y = directions[item_index]
                new_i, new_j = x+i, y+j
                if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len and (new_i, new_j) not in recursion_stack:
                    current_diff = abs(heights[new_i][new_j]-current_val)
                    if min_val is not None and current_diff >= min_val:
                        continue
                    val = dfs(new_i, new_j, recursion_stack, direction_keys[item_index])
                    if val is None:
                        continue
                    current_max = max(val, current_diff)
                    if min_val is None or current_max < min_val:
                        min_val = current_max
            recursion_stack.remove((i,j))
            memo[(i,j,dir)] = min_val
            return min_val
        return dfs(0,0, set(), "Down")

sol = Solution()
print(sol.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(sol.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(sol.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
print(sol.minimumEffortPath([[3]]))
print(sol.minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]))
print(sol.minimumEffortPath([[10,8],[10,8],[1,2],[10,3],[1,3],[6,3],[5,2]]))
#print(sol.minimumEffortPath([[8,3,2,5,2,10,7,1,8,9],[1,4,9,1,10,2,4,10,3,5],[4,10,10,3,6,1,3,9,8,8],[4,4,6,10,10,10,2,10,8,8],[9,10,2,4,1,2,2,6,5,7],[2,9,2,6,1,4,7,6,10,9],[8,8,2,10,8,2,3,9,5,3],[2,10,9,3,5,1,7,4,5,6],[2,3,9,2,5,10,2,7,1,8],[9,10,4,10,7,4,9,3,1,6]]))