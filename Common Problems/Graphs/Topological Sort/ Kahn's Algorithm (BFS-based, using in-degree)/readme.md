# Kahn's Algorithm (BFS-based Topological Sort)

## 1. Overview
- **What is it?** A queue-based algorithm for producing a valid ordering of vertices in a directed graph where each edge represents a dependency. It repeatedly removes nodes with no incoming dependencies, which makes it a natural fit for topological sorting.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#topological-sort` `#queue` `#cycle-detection`

## 2. Problem It Solves
It solves the problem of ordering tasks or events when some must happen before others, such as course prerequisites or build steps. Without it, dependency-heavy workflows can become ambiguous or impossible to schedule correctly.

## 3. Approach / Intuition
Think of this as repeatedly removing the tasks that are currently available to start, like turning a dependency graph into a queue of ready work.
- Compute the in-degree of every vertex.
- Start with all vertices whose in-degree is zero and place them in a queue.
- Remove one vertex at a time, append it to the result, and reduce the in-degree of its neighbors.
- Whenever a neighbor reaches zero in-degree, add it to the queue.
- If the algorithm does not process every vertex, the graph contains a cycle and no valid ordering exists.

## 4. Pseudocode
```text
function topo_sort_kahn(graph):
    compute in-degree for every vertex
    create empty queue
    create empty order list

    for each vertex in graph:
        if in-degree[vertex] == 0:
            add vertex to queue

    while queue is not empty:
        node = remove from front of queue
        append node to order

        for each neighbor of node:
            decrement in-degree[neighbor]
            if in-degree[neighbor] == 0:
                add neighbor to queue

    if length(order) != number of vertices:
        raise error "Graph has a cycle"

    return order
```

## 5. Assumptions & Constraints
- Assumes the input is a directed graph represented as an adjacency list.
- Works for directed acyclic graphs and raises an error when a cycle is found.
- Handles isolated vertices and disconnected components.
- Does not support edge weights because the goal is ordering, not shortest path.
- Produces one valid topological order, not necessarily the only one.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | Each vertex and edge is processed once when the graph is simple and acyclic. |
| Average | O(V + E) | O(V) | The algorithm scales linearly with the graph size. |
| Worst | O(V + E) | O(V) | Even a dense graph still requires processing each edge and vertex once. |

- The worst case remains linear because each edge is examined only once while decrementing in-degrees and each vertex enters the queue at most once.

## 7. Real-Life Use Cases
- Course planning: schedule classes after their prerequisites are completed.
- Build pipelines: compile or test modules in dependency-safe order.
- Package installation: install libraries only after their dependencies are ready.
- Workflow automation: run tasks in a sequence that respects upstream dependencies.

## 8. Comparison / When to Use vs Alternatives
- Compared to DFS-based topological sort: Kahn's algorithm is iterative and often easier to implement with a queue when you want a straightforward "ready tasks first" approach.
- Compared to DFS: DFS naturally integrates cycle detection with recursion, while Kahn's algorithm is often more intuitive for dependency scheduling.

## 9. Common Mistakes / Gotchas
- Forgetting to initialize the in-degree for every vertex before processing edges.
- Using the wrong queue behavior, such as adding nodes in the wrong order or processing the queue incorrectly.
- Assuming a graph with a cycle can still produce a valid topological order.
- Not checking whether all vertices were processed at the end.

## 10. Code Reference
- Path: `Common Problems/Graphs/Topological Sort/ Kahn's Algorithm (BFS-based, using in-degree)/kahn_bfs_based.py`
- Implements a queue-based topological sort using in-degree tracking and raises an error if a cycle is detected.

## 11. Related Topics
- See also: [DFS-based Topological Sort](../DFS based Topological Sort/README.md)
- Related: [Cycle Detection in Graphs](../../Graphs/Cycle Detection/README.md)

## 12. References
- CLRS, Introduction to Algorithms, Chapter on Topological Sort.
