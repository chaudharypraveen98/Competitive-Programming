# Union-Find

## 1. Overview
- **What is it?** Union-Find is a data structure used to track connected components in a graph or set of elements, especially when we repeatedly add edges and ask whether two nodes are already connected.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#union-find` `#cycle-detection` `#traversal`

## 2. Problem It Solves
It helps answer questions like “are these two nodes connected?” or “will adding this edge create a cycle?” efficiently without rebuilding the structure each time.

## 3. Approach / Intuition
Think of each element as belonging to a family tree. The structure supports two main operations:
- `find(x)` locates the representative of the set containing `x`.
- `union(x, y)` merges the two sets if they are different.
- Path compression and union by rank keep the operations very fast in practice.

## 4. Pseudocode
```text
function find(x):
    if parent[x] is not x:
        parent[x] = find(parent[x])
    return parent[x]

function union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return False
    attach smaller tree under larger tree
    return True
```

## 5. Assumptions & Constraints
- Assumes the items are identified by integers or comparable labels.
- Works well when the same set of elements is updated repeatedly.
- Handles disconnected groups naturally.
- Does not directly store the path between elements; it only tracks connectivity.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(α(n)) | O(n) | Nearly constant time for each operation |
| Average | O(α(n)) | O(n) | In practice, very fast due to path compression and union by rank |
| Worst | O(α(n)) | O(n) | The inverse Ackermann function grows extremely slowly |

- The worst case remains almost constant because the union-find operations are amortized very efficiently.

## 7. Real-Life Use Cases
- Detecting cycles in graphs while building a spanning tree.
- Managing connected components in social networks and network routing.
- Grouping related items in image processing or clustering problems.

## 8. Comparison / When to Use vs Alternatives
- Use Union-Find when you need fast connectivity checks and merges over many operations.
- Compared with DFS, it is better for repeated dynamic connectivity queries.
- Compared with BFS, it is more compact when the main task is to know whether two items are connected.

## 9. Common Mistakes / Gotchas
- Forgetting to use path compression or union by rank, which can make the structure slower.
- Confusing the representative root with the original element.
- Calling `union` on already-connected components unnecessarily.

## 10. Code Reference
- `union_find.py`
- Implements a simple Union-Find structure with `find` and `union` operations.

## 11. Related Topics
- See also: [Graphs overview](../../readme.md)
- Related topics: cycle detection, Kruskal’s algorithm, and connected components.

## 12. References
- CLRS, Introduction to Algorithms, chapter on disjoint-set data structures.
- Standard interview notes on Union-Find and connectivity.

