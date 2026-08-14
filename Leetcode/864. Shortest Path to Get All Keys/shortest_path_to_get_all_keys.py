from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        WALL = "#"
        START = "@"
        EMPTY = "."
        available_keys = ""
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])
        def is_key(val):
            return 96<ord(val)<123
        start_index = None
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == START:
                    start_index = (i,j)
                elif is_key(val):
                    available_keys +=val
        queue = deque([start_index+(0,0)])
        visited = {start_index}
        total_keys_in_bitwise = (1<<len(available_keys))-1

        while queue:
            x,y, cost, acquired_keys = queue.popleft()
            val = grid[x][y]
            if val != EMPTY and val != START:
                if val in available_keys:
                    acquired_keys = acquired_keys | 1 << (ord(val)-ord('a'))
                    if acquired_keys==total_keys_in_bitwise:
                        return cost
                else:
                    has_key = (acquired_keys >> (ord(val.lower())-ord('a'))) & 1
                    if not has_key:
                        continue

            for nr, nc in directions:
                new_x, new_y = x+nr, y+nc
                new_tuple = (new_x, new_y, acquired_keys)
                if new_tuple not in visited and new_x>=0 and new_x <m and new_y>=0 and new_y<n and grid[new_x][new_y] != WALL:
                    visited.add(new_tuple)
                    queue.append((new_x, new_y, cost+1, acquired_keys))
        return -1

sol = Solution()
print(sol.shortestPathAllKeys(["@.a..","###.#","b.A.B"]))
print(sol.shortestPathAllKeys(["@..aA","..B#.","....b"]))
print(sol.shortestPathAllKeys(["@Aa"]))
print(sol.shortestPathAllKeys(["..#....##.","....d.#.D#","#...#.c...","..##.#..a.","...#....##","#....b....",".#..#.....","..........",".#..##..A.",".B..C.#..@"]))

# . . # . . . . # # .
# . . . . d . # . D #
# # . . . # . c . . .
# . . # # . # . . a .
# . . . # . . . . # #
# # . . . . b . . . .
# . # . . # . . . . .
# . . . . . . . . . .
# . # . . # # . . A .
# . B . . C . # . . @