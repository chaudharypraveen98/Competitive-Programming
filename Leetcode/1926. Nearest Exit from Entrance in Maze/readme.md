# [1926. Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/)

## Description
- Return the minimum number of steps needed to reach any exit cell from the given entrance.
- You can move up, down, left, or right through open cells (.) and cannot pass through walls (+).

## Key idea
- This is a shortest-path problem on an unweighted grid.
- A simple BFS from the entrance finds the nearest exit in the fewest moves.

## Approach
### Solution 1: BFS from the entrance
1. Start a queue with the entrance position and distance 0.
2. Mark the entrance as visited.
3. Pop a cell from the queue and check if it is on the boundary and not the entrance.
4. If it is an exit, return the current distance.
5. Explore all valid neighbors and push them into the queue with an increased distance.

### Solution 2: BFS with distance tracking
1. Store each queue item as (row, col, steps).
2. Keep a visited set to avoid revisiting the same cell.
3. When a boundary cell is reached, return its stored distance.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## Notes
- BFS works well because every move has the same cost.
- The entrance itself is not considered an exit, even if it is on the border.