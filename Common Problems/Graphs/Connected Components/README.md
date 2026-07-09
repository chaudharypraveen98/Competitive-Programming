# Connected Components

## 1. Overview
- **What is it?** A connected component is a subset of vertices in an undirected graph where every vertex can reach every other vertex by some path.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#traversal`

## 2. Problem It Solves
- It identifies isolated groups in an undirected graph so we can treat each group independently and avoid assuming the graph is fully connected.

## 3. Approach / Intuition
- Imagine exploring a group of friends where you start from one person and follow every friendship until you can no longer reach anyone new.
- Each time you start from an unvisited vertex, you discover one full connected component.
- Use BFS or DFS to collect all vertices reachable from that starting vertex.
- Repeat until every vertex has been visited.

## 4. Pseudocode
```
function connected_components(graph):
    visited = empty set
    components = []
    for each vertex in graph:
        if vertex not in visited:
            component = explore_component(graph, vertex, visited)
            components.append(component)
    return components

function explore_component(graph, start, visited):
    stack_or_queue = [start]
    component = []
    visited.add(start)
    while stack_or_queue is not empty:
        node = remove one item from stack_or_queue
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                add neighbor to stack_or_queue
    return component
```

## 5. Assumptions & Constraints
- Input assumes an undirected graph represented by an adjacency list.
- Handles empty graphs, single-node graphs, fully disconnected graphs, and multiple separate components.
- Assumes vertices can be any hashable values.
- Does not handle directed-graph strongly connected components; that is a different algorithm.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | Visiting each vertex and edge once when the graph is connected or sparsely connected. |
| Average | O(V + E) | O(V) | Every edge and vertex is processed exactly once across all components. |
| Worst | O(V + E) | O(V) | Dense graphs still require scanning every edge and vertex in the adjacency list. |

- The worst case occurs when the graph is fully connected or contains many edges, so traversal must visit every vertex and edge.

## 7. Real-Life Use Cases
- Network analysis: find isolated subnetworks in a social graph or computer network.
- Image processing: identify connected pixel regions in binary images.
- Biology: group interacting proteins or genes in an interaction network.
- Clustering: detect independent clusters in an undirected similarity graph.

## 8. Comparison / When to Use vs Alternatives
- Connected components vs BFS/DFS alone: use connected components when you need to partition the entire graph into reachable groups, not just explore from one start node.
- Connected components vs Strongly Connected Components: use this for undirected graphs; use SCC algorithms like Kosaraju or Tarjan for directed graphs.

## 9. Common Mistakes / Gotchas
- Forgetting to mark nodes as visited when they are enqueued/pushed, causing duplicate exploration or infinite loops.
- Assuming the graph is connected and only running one traversal from the first vertex.
- Using a structure that removes from the wrong end and accidentally implementing the wrong order, though either BFS or DFS works for components.

## 10. Code Reference
- `Common Problems/Graphs/Connected Components/connected_components.py`
- Implements both BFS- and DFS-based connected component discovery for undirected graphs.

## 11. Related Topics
- See also: `../Depth First Search/README.md`, `../Breadth First Search/README.md`

## 12. References (optional)
- N/A
