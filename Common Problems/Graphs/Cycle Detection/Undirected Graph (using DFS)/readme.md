# Cycle Detection in an Undirected Graph (Using DFS)

## 1. Overview
- **What is it?** This approach checks whether an undirected graph contains a cycle by running DFS and tracking the parent of each node.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#cycle-detection` `#dfs` `#traversal`

## 2. Problem It Solves
In an undirected graph, simply seeing a node again is not enough to prove a cycle because the DFS may revisit the parent edge. Tracking the parent avoids this mistake and correctly identifies real cycles.

## 3. Approach / Intuition
Think of DFS like exploring a maze while keeping track of the path you came from. If you encounter a neighbor that is already on the current path and is not the parent, then you have found a cycle.
- Start DFS from each unvisited vertex.
- Keep track of the current node's parent.
- For each neighbor, skip the parent edge.
- If another already-visited node is found, report a cycle.
- Continue until all components are checked.

## 4. Pseudocode
```text
function has_cycle_undirected(graph):
    visited = empty set

    function dfs(node, parent):
        visited.add(node)
        for each neighbor in graph[node]:
            if neighbor is parent:
                continue
            if neighbor in visited:
                return True
            if dfs(neighbor, node):
                return True
        return False

    for each node in graph:
        if node not in visited and dfs(node, null):
            return True

    return False
```

## 5. Assumptions & Constraints
- Assumes the graph is stored as an adjacency list.
- Works for undirected graphs, where each edge appears in both directions.
- Handles disconnected graphs by checking every component.
- Treats self-loops as cycles.
- Does not return the actual cycle path, only a boolean result.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | A tree or acyclic graph is processed in linear time |
| Average | O(V + E) | O(V) | Each vertex and edge is explored once |
| Worst | O(V + E) | O(V) | Dense graphs still require linear work in the size of the graph |

- The worst case occurs when the graph is dense, but the algorithm still remains linear because each edge is examined a constant number of times.

## 7. Real-Life Use Cases
- Social networks: detecting whether a friend connection graph contains a loop.
- Network design: checking whether a communication network has circular routing paths.
- Roadmaps: verifying whether an undirected road network has a closed loop.

## 8. Comparison / When to Use vs Alternatives
- Use this when the graph is undirected and you want a simple cycle check.
- This is different from the directed-graph version because the parent edge must be ignored explicitly.
- Compared with union-find, this approach is more intuitive for DFS-based reasoning and path exploration.

## 9. Common Mistakes / Gotchas
- Treating any visited neighbor as a cycle, even when it is the immediate parent.
- Forgetting to check all disconnected components.
- Confusing undirected and directed graph behavior, since the rules are different.
- Missing the case of a self-loop, which should be considered a cycle.

## 10. Code Reference
- `undirected_graph_cycle_detection.py`
- Implements cycle detection for undirected graphs using DFS with parent tracking.

## 11. Related Topics
- See also: [Graphs overview](../../../readme.md)
- Related ideas: DFS traversal, directed-graph cycle detection, and topological sort.

## 12. References
- Standard DFS graph traversal notes.
- Common interview practice for undirected graph cycle detection.
