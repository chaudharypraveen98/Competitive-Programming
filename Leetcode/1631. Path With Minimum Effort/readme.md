# [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/description/)

## Why Traditional Paradigms Break Down

To see why Dijkstra's algorithm is required for 4-directional grid problems like **Path With Minimum Effort**, consider why other common algorithmic paradigms fail:

---

### 1. Dynamic Programming (DP) Fails
* **Requirement:** Standard DP requires a **Directed Acyclic Graph (DAG)** where subproblems have a strict, unidirectional evaluation order (e.g., only moving **Right** and **Down**).
* **The Breakdown:** When movement is 4-directional (**Up**, **Down**, **Left**, **Right**), the graph naturally contains **cycles**. 
* **Circular Dependency:** The optimal path to cell $(r, c)$ might depend on $(r + 1, c)$, whose optimal path might recursively depend on $(r, c - 1)$ or $(r, c)$ itself, creating infinite circular dependencies that standard memoization/tabulation cannot resolve.

---

### 2. Standard BFS Fails
* **Requirement:** Standard Breadth-First Search (BFS) computes the shortest path exclusively on **unweighted graphs** (or graphs where every edge has identical cost).
* **The Breakdown:** The grid is an explicitly **weighted graph** where each step has a dynamic transition cost:
  
  $$\text{weight} = |heights[r_1][c_1] - heights[r_2][c_2]|$$

* **Suboptimal Cost:** A path with fewer total steps does not guarantee a lower bottleneck effort. Standard BFS explores by hop-count rather than path cost, causing it to discover high-effort paths first.

---

### 3. DFS / Backtracking Fails
* **Requirement:** Viable when all possible paths must be exhaustively checked or pruned aggressively with a strict heuristic.
* **The Breakdown:** DFS does not evaluate paths in order of cost. It traverses arbitrarily deep into non-optimal branches, necessitating exhaustive search across the entire search space.
* **Complexity Explosion:** For an $R \times C$ grid, the time complexity scales exponentially to **$\mathcal{O}(4^{R \cdot C})$**, triggering a **Time Limit Exceeded (TLE)** on dense grids.

---

## Comparison Summary

| Paradigm | Primary Failure Mode | Complexity Impact |
| :--- | :--- | :--- |
| **Dynamic Programming** | Fails on cyclic dependencies from 4-way movement. | State recursion cannot resolve. |
| **Standard BFS** | Ignores non-uniform edge weights; prioritizes hop count. | Yields incorrect/suboptimal answers. |
| **DFS / Backtracking** | Exhaustive path traversal without cost-ordered priority. | Exponential $\mathcal{O}(4^{R \cdot C})$ (TLE). |
| **Dijkstra (Priority Queue)** | Greedily expands minimum-effort paths first. | Optimal $\mathcal{O}(R \cdot C \log(R \cdot C))$. |
