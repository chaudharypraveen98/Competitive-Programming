## [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

### Approach
1. Use krushkal or prism to get min cost

### The general lesson worth keeping

Kruskal's and Prim's are asymptotically different specifically based on graph density:

Sparse graphs (E close to V, not V²) → Kruskal's tends to win, since sorting a small edge list is cheap.
Dense graphs (E close to V², like this problem — every point connects to every other point) → array-based Prim's tends to win, since it avoids the sort entirely and a heap's log-factor doesn't pay for itself when nearly every edge exists anyway.


## Optimized Prim's Algorithm ($O(N^2)$) Summary

### Overview
Prim's Algorithm finds the **Minimum Spanning Tree (MST)** of a connected, edge-weighted undirected graph. While standard Prim's uses a Min-Heap (Priority Queue) and is optimal for **sparse graphs**, **Optimized Prim's** uses a simple array (`min_dist`) and is optimal for **dense/complete graphs** where $E \approx V^2$.

---

### Key Differences: Standard vs. Optimized Prim's

| Feature | Standard Prim's (Heap-Based) | Optimized Prim's (Array-Based) |
| :--- | :--- | :--- |
| **Data Structure** | Min-Heap / Priority Queue | 1D Array (`min_dist` of size $N$) |
| **Time Complexity** | $O(E \log V) \implies O(N^2 \log N)$ on complete graphs | $O(V^2) \implies O(N^2)$ on complete graphs |
| **Space Complexity**| $O(E) \implies O(N^2)$ | $O(V) \implies O(N)$ |
| **Best Graph Type** | **Sparse Graphs** ($E \approx V$) | **Dense/Complete Graphs** ($E \approx V^2$) |
| **Edge Storage** | Requires explicit adjacency list / edge list | **Implicit / On-the-fly** (No adjacency list needed) |

---

### Mental Model: "The Best-Price Board"

* **Standard Prim's ("The To-Do List"):** Pushes every candidate edge onto a giant pile (Min-Heap). As the graph gets denser, the pile grows to $N^2$ edges, requiring heavy overhead to push, pop, and discard invalid duplicate edges.
* **Optimized Prim's ("The Best-Price Board"):** Maintains a chalkboard listing $N$ unvisited nodes and the **cheapest cost to connect each to the current MST**. When a new node joins the MST, it checks if it can lower the cost for any unvisited nodes and **overwrites** their values in $O(1)$ time.

---

### Algorithm Blueprint

1. **Initialize Arrays:**
   * `min_dist`: Array of size $N$, filled with $\infty$. Set `min_dist[0] = 0`.
   * `visited`: Boolean array of size $N$, filled with `False`.
2. **Loop $N$ Times:**
   * **Select:** Scan `min_dist` to find the unvisited node `u` with the smallest value.
   * **Add:** Mark `visited[u] = True` and add `min_dist[u]` to `total_cost`.
   * **Update:** Loop through all unvisited nodes `v`. Compute distance from `u` to `v`. If `dist(u, v) < min_dist[v]`, update `min_dist[v] = dist(u, v)`.
3. **Return:** `total_cost`.

---

### Pseudocode

```text
Algorithm OptimizedPrimsMST(points):
    N = length(points)
    min_dist = array of size N initialized to INFINITY
    visited  = array of size N initialized to FALSE
    
    min_dist[0] = 0
    total_cost  = 0

    FOR step FROM 0 TO N - 1 DO:
        // 1. Pick unvisited node with smallest distance
        u = -1
        FOR i FROM 0 TO N - 1 DO:
            IF NOT visited[i] AND (u == -1 OR min_dist[i] < min_dist[u]) THEN:
                u = i
            END IF
        END FOR

        // 2. Add 'u' to MST
        visited[u] = TRUE
        total_cost = total_cost + min_dist[u]

        // 3. Relax edges to all unvisited neighbors
        FOR v FROM 0 TO N - 1 DO:
            IF NOT visited[v] THEN:
                dist = ManhattanDistance(points[u], points[v])
                IF dist < min_dist[v] THEN:
                    min_dist[v] = dist
                END IF
            END IF
        END FOR

    END FOR

    RETURN total_cost