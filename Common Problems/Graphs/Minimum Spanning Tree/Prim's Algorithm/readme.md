# Prim's Algorithm

## 1. Overview
- **What is it?** Prim's Algorithm finds a minimum spanning tree (MST) for a connected, weighted graph by growing the tree one vertex at a time, always adding the cheapest edge connecting the tree to an unvisited vertex.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#mst` `#heap` `#greedy`

## 2. Problem It Solves
Similar to Kruskal's, but uses a different strategy: instead of sorting all edges globally, Prim grows the tree from a starting vertex, repeatedly adding the nearest unvisited vertex to the current tree.

## 3. Approach / Intuition
Think of it as expanding a region step by step. Start at one vertex and keep adding the closest unvisited vertex.
- Begin with a starting vertex in the tree.
- Use a min-heap to track the cheapest edge connecting the tree to unvisited vertices.
- Repeatedly pop the cheapest edge; if it connects to an unvisited vertex, add that vertex to the tree.
- Continue until all reachable vertices are in the tree.

## 4. Pseudocode
```text
function prim(graph, start):
    visited = {start}
    heap = empty min-heap
    mst_edges = empty list
    total_weight = 0

    push all edges from start into heap

    while heap is not empty:
        weight, u, v = pop minimum from heap
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight = total_weight + weight
        push all edges from v into heap

    return total_weight, mst_edges
```

## 5. Assumptions & Constraints
- Assumes the graph is weighted and undirected.
- Requires a starting vertex to begin the algorithm.
- Handles disconnected graphs by returning the MST for the component containing the starting vertex.
- Works with positive weights.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(E log V) | O(V) | When the graph is sparse and the starting vertex connects quickly to the tree |
| Average | O(E log V) | O(V) | Heap operations dominate; each edge is considered once |
| Worst | O(E log V) | O(V) | Dense graphs have many edges, but the heap-based approach is still efficient |

- The worst case remains logarithmic in V due to the heap, making Prim efficient even for dense graphs compared to Kruskal's edge-sorting overhead.

## 7. Real-Life Use Cases
- Building a minimum-cost network starting from a central hub or office.
- Expanding a wireless network from a single access point to cover all areas cheaply.
- Growing a power grid or infrastructure from a central location outward.

## 8. Comparison / When to Use vs Alternatives
- Use Prim's when you want to grow an MST from a specific starting vertex.
- Kruskal sorts all edges upfront and selects the cheapest globally; Prim grows locally from a starting point.
- Prim is often better for dense graphs (fewer edge sorting overhead); Kruskal is better for sparse graphs.

## 9. Common Mistakes / Gotchas
- Adding an edge to an already-visited vertex (solved by checking `if v in visited`).
- Forgetting to use a heap, causing O(V²) complexity.
- Not handling disconnected graphs; the algorithm will only find an MST for the reachable component.

## 10. Code Reference
- `prims.py`
- Implements Prim's Algorithm using a min-heap, starting from a given vertex.

## 11. Related Topics
- See also: [Graphs overview](../../../readme.md), [Kruskal's Algorithm](../Kruskal's%20Algorithm/readme.md)
- Related topics: Minimum spanning trees, greedy algorithms, and heap operations.

## 12. References
- CLRS, Introduction to Algorithms, chapter on minimum spanning trees.
- Standard graph theory notes on MST algorithms.
