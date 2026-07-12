# Kruskal's Algorithm

## 1. Overview
- **What is it?** Kruskal's Algorithm finds a minimum spanning tree (MST) for a connected, weighted graph by selecting the cheapest edges without creating cycles.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#mst` `#union-find` `#sorting`

## 2. Problem It Solves
When a network or graph has weighted connections, Kruskal's Algorithm helps build the cheapest possible structure that connects all vertices while avoiding redundant links.

## 3. Approach / Intuition
Think of it as building a network one cheap connection at a time.
- Sort all edges by weight from smallest to largest.
- Take the smallest edge if it connects two different components.
- Keep adding edges until all vertices are connected or no more valid edges remain.
- Union-Find is used to check whether adding an edge would create a cycle.

## 4. Pseudocode
```text
function kruskal(vertices, edges):
    sort edges by weight
    create union-find structure for vertices
    mst = empty list
    total_weight = 0

    for each edge (u, v, w) in sorted edges:
        if union(u, v) succeeds:
            add edge to mst
            total_weight = total_weight + w
        if mst has V - 1 edges:
            break

    return total_weight, mst
```

## 5. Assumptions & Constraints
- Assumes the graph is weighted.
- Works for undirected graphs.
- Handles disconnected graphs by building a minimum spanning forest instead of a single spanning tree.
- Does not handle negative-weight-specific advantages differently; the algorithm still works with negative weights.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(E log E) | O(V) | Sorting dominates when edges are already nearly ordered |
| Average | O(E log E) | O(V) | Sorting edges is the main cost |
| Worst | O(E log E) | O(V) | Dense graphs still follow the same sorting-based bound |

- The worst case is driven by sorting the edges, which dominates the runtime for most practical inputs.

## 7. Real-Life Use Cases
- Designing the cheapest network cable layout between cities.
- Building efficient road or power-line connections with minimum total cost.
- Creating cluster or connectivity structures in computer networks.

## 8. Comparison / When to Use vs Alternatives
- Use Kruskal's Algorithm when you want a minimum spanning tree for a weighted undirected graph.
- Prim's Algorithm is another MST approach; Prim grows the tree from a starting node, while Kruskal grows it from the smallest edges.
- Compared with DFS-based approaches, Kruskal is more natural when edges are sorted by cost.

## 9. Common Mistakes / Gotchas
- Forgetting to use Union-Find to detect cycles.
- Adding an edge that connects vertices already in the same component.
- Stopping too early before collecting enough edges for a spanning tree.

## 10. Code Reference
- `kruskal.py`
- Implements Kruskal's Algorithm using a Union-Find structure and sorted edges.

## 11. Related Topics
- See also: [Graphs overview](../../../readme.md)
- Related topics: Prim's Algorithm, Union-Find, and cycle detection.

## 12. References
- CLRS, Introduction to Algorithms, chapter on minimum spanning trees.
- Standard graph theory notes on MST algorithms.
