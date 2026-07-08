# DFS-based Topological Sort

## 1. Overview
- **What is it?** A graph algorithm that produces a valid ordering of tasks such that every dependency appears before the task that depends on it. It uses depth-first search and a finishing order to build the result.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#topological-sort` `#cycle-detection` `#traversal`

## 2. Problem It Solves
It solves the problem of ordering dependent tasks, such as course prerequisites or build steps, when the dependency relationships form a directed acyclic graph. It also detects whether the graph contains a cycle, in which case no valid ordering exists.

## 3. Approach / Intuition
Think of this as exploring a dependency chain until you reach the end, then recording the task after all its requirements are handled.
- Start from each unvisited vertex and perform DFS.
- Mark a vertex as "in progress" while it is on the current recursion path.
- If a neighbor is encountered that is still "in progress", a cycle exists.
- After all neighbors are processed, mark the vertex as complete and add it to a stack.
- Reverse the stack at the end to obtain a valid topological order.

## 4. Pseudocode
```text
function topo_sort_dfs(graph):
    initialize color for every vertex as WHITE
    create empty stack

    function dfs(node):
        color[node] = GRAY

        for each neighbor in graph[node]:
            if color[neighbor] == GRAY:
                raise error "Graph has a cycle"
            if color[neighbor] == WHITE:
                dfs(neighbor)

        color[node] = BLACK
        push node onto stack

    for each vertex in graph:
        if color[vertex] == WHITE:
            dfs(vertex)

    return reverse(stack)
```

## 5. Assumptions & Constraints
- Assumes the input is a directed graph represented as an adjacency list.
- Works for directed acyclic graphs and raises an error when a cycle is found.
- Handles a single vertex, disconnected components, and multiple roots.
- Does not support weighted edges; it only cares about dependency order.
- Does not return all possible valid orders, only one valid topological ordering.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | Each vertex and edge is processed once in a simple DAG. |
| Average | O(V + E) | O(V) | The traversal cost remains linear in the size of the graph. |
| Worst | O(V + E) | O(V) | A dense graph still requires visiting every vertex and edge once. |

- The main reason the worst case is still linear is that each edge is examined at most once during DFS, and the extra bookkeeping is proportional to the number of vertices.

## 7. Real-Life Use Cases
- Build systems: determine the order to compile modules when one depends on another.
- University course planning: schedule classes only after prerequisites are completed.
- Package managers: install dependencies in a safe order.
- Project workflows: order tasks in a pipeline where some steps must finish before others begin.

## 8. Comparison / When to Use vs Alternatives
- Compared to Kahn's algorithm: DFS is a good fit when you want a recursive or stack-based approach and cycle detection is naturally integrated.
- Compared to BFS-based topological sort: DFS is often simpler to reason about for dependency trees and recursion-based implementations, while Kahn's algorithm is iterative and may feel more direct for queue-based processing.

## 9. Common Mistakes / Gotchas
- Forgetting to distinguish between WHITE, GRAY, and BLACK states, which can cause incorrect cycle detection.
- Appending a node to the stack before exploring its neighbors, which would produce the wrong order.
- Misinterpreting a cycle as a valid ordering issue instead of handling it explicitly.
- Assuming every graph has a topological order; only DAGs do.

## 10. Code Reference
- Path: `Common Problems/Graphs/Topological Sort/DFS based Topological Sort/dfs_based_topological_sort.py`
- Implements an iterative DFS-style solution using a color-state approach and a finishing stack to produce a valid topological order.

## 11. Related Topics
- See also: [Kahn's Algorithm (BFS-based)](../Kahn's Algorithm (BFS-based, using in-degree)/README.md)
- Related: [Cycle Detection in Graphs](../../Graphs/Cycle Detection/README.md)

## 12. References
- CLRS, Introduction to Algorithms, Chapter on Topological Sort and DFS.
