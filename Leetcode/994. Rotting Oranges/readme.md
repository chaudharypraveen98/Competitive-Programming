# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)

### Appraoch
When multiple starting points spread **simultaneously**, seed *all* of them into
the BFS queue together as one batch — don't run separate BFS per source and
combine results afterward. Combining separate single-source results (even with
`min()`) does **not** correctly model simultaneous spread from multiple directions.

### Pattern to Remember
1. Scan the grid once, collect all source cells into a list, mark them `visited`
   **immediately** (before BFS starts).
2. Push that whole list as **one batch** into the queue.
3. Process one full batch (`temp_res` / current level) per BFS iteration — this
   batch represents "everything that changed in one time step." Increment your
   counter **once per batch**, not once per cell.
4. Stop when the queue is empty.
5. Do a final scan for any leftover, unreached target cells (the `-1` check) —
   this catches unreachable/disconnected fresh oranges.

### Why Marking Sources Visited Upfront Mattered
Marking all initial rotten cells `visited` before BFS begins prevents the
traversal from ever re-discovering another rotten cell as if it were "newly
infected" — this sidesteps the need for a stricter value check inside the
BFS loop (e.g. distinguishing "fresh" vs "already rotten" by value).

### General Lesson
Whenever a problem says **"at the same time" / "simultaneously"** / gives you
multiple starting points with equal footing — that's the signal for
**multi-source BFS**, seeded as one batch, not N separate single-source
traversals.

### Related Topics
- See also: BFS, Number of Islands (single-source grid BFS)