## [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

### Approach
1. Use krushkal or prism to get min cost

### The general lesson worth keeping

Kruskal's and Prim's are asymptotically different specifically based on graph density:

Sparse graphs (E close to V, not V²) → Kruskal's tends to win, since sorting a small edge list is cheap.
Dense graphs (E close to V², like this problem — every point connects to every other point) → array-based Prim's tends to win, since it avoids the sort entirely and a heap's log-factor doesn't pay for itself when nearly every edge exists anyway.