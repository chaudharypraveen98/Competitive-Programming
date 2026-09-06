## [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/)

### Approach
- **Minimum Spanning Tree (MST)**: A subset of edges connecting all $n$ nodes with minimum total weight using exactly $n - 1$ edges.
- **Critical Edge**: An edge present in every MST. Removing it either disconnects the graph or forces the MST total weight to increase.
- **Pseudo-Critical Edge**: An edge that can appear in at least one MST, but is not critical. Forcing it into the tree still yields the optimal baseline MST weight.
- **Preserve Original Ordering**: Kruskal's requires sorting by weight ascending, but output demands original edge indices. Attach original indices before sorting.