# Cycle Detection in a Directed Graph (Using Colors)

## 1. Overview
- **What is it?** This approach detects whether a directed graph contains a cycle by marking each node as unvisited, currently exploring, or fully explored during DFS.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#cycle-detection` `#dfs` `#traversal`

## 2. Problem It Solves
In directed graphs, a simple parent-based check does not work well because the graph can have one-way edges. The color-based DFS method helps identify back-edges that indicate a cycle.

## 3. Approach / Intuition
Think of DFS as walking through the graph while coloring each node to show where it is in the current search.
- Use three states: WHITE for unvisited, GRAY for currently in the recursion path, and BLACK for fully processed.
- When a GRAY neighbor is found, a cycle exists.
- When a WHITE neighbor is found, recurse into it.
- Mark the node BLACK after all its neighbors are processed.

## 4. Pseudocode
```text
function has_cycle_directed(graph):
    color = map each node to WHITE

    function dfs(node):
        color[node] = GRAY
        for each neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for each node in graph:
        if color[node] == WHITE and dfs(node):
            return True

    return False
```

## 5. Assumptions & Constraints
- Assumes the graph is represented using an adjacency list.
- Works for directed graphs and detects cycles through back-edges.
- Handles disconnected graphs by running DFS from each unvisited node.
- Treats self-loops as cycles.
- Does not return the exact cycle path, only a boolean result.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | A graph with no edges or a simple acyclic structure is processed quickly |
| Average | O(V + E) | O(V) | Each node and edge is examined once during DFS |
| Worst | O(V + E) | O(V) | Dense directed graphs still require linear work in terms of vertices and edges |

- The worst case occurs when the DFS explores many edges, but the algorithm remains linear because each edge is visited a constant number of times.

## 7. Real-Life Use Cases
- Build systems: detecting circular dependencies between packages or modules.
- Scheduling problems: checking whether tasks depend on themselves indirectly.
- Compiler and dependency analysis: finding recursive imports or cyclic references.

## 8. Comparison / When to Use vs Alternatives
- This is a clean and standard choice when you want to detect cycles in a directed graph.
- It is similar to the recursion-stack approach, but it expresses the state more explicitly with three colors.
- It is often preferred in interviews and textbooks because the state model is easy to explain and reason about.

## 9. Common Mistakes / Gotchas
- Forgetting to change a node from GRAY to BLACK after finishing its DFS branch.
- Confusing GRAY with BLACK and accidentally reporting a cycle for already-processed nodes.
- Not initializing all nodes with the WHITE state.
- Checking only one starting node when the graph may be disconnected.

## 10. Code Reference
- `colors.py`
- Implements directed-graph cycle detection using DFS and the WHITE/GRAY/BLACK coloring strategy.

## 11. Related Topics
- See also: [Graphs overview](../../../readme.md)
- Related ideas: DFS traversal, topological sort, and cycle detection using a recursion stack.

## 12. References
- Standard DFS and graph traversal notes.
- CLRS-style explanations of cycle detection in directed graphs.
