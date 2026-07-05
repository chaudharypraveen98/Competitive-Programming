# BFS Shortest Path

## 1. Overview
- **What is it?** BFS Shortest Path is a graph-search technique used to find the minimum number of edges between a start node and a target node in an unweighted graph.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#traversal` `#shortest-path`

## 2. Problem It Solves
It solves the problem of finding a valid path from a start node to a target node while minimizing hop count. A plain traversal or DFS may find a path, but it does not guarantee that the path has the fewest edges.

## 3. Approach / Intuition
Think of it like ripples spreading outward from the start: you explore every node one layer at a time.
- Start from the source and place its initial path into a queue.
- Repeatedly remove the next path from the queue and inspect its last node.
- If the last node equals the target, return that path.
- For each unvisited neighbor, mark it visited and enqueue a new path that extends the current path.
- Stop once the target is found or the queue becomes empty.

## 4. Pseudocode
```text
function shortest_path_bfs(graph, start, target):
    queue = empty queue
    enqueue [start]
    visited = set containing start

    while queue is not empty:
        path = dequeue from front
        node = last element of path

        if node == target:
            return path

        for each neighbor of node:
            if neighbor not in visited:
                add neighbor to visited
                enqueue copy of path extended with neighbor

    return None
```

## 5. Assumptions & Constraints
- Assumes the graph is unweighted.
- Works for both directed and undirected graphs, depending on how edges are added.
- Requires the graph to be represented as an adjacency list.
- Handles disconnected graphs by returning None when the target is unreachable.
- Does not guarantee correct results for weighted graphs; Dijkstra is the better choice there.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | The target is the start node, so the algorithm stops immediately. |
| Average | O(V + E) | O(V) | Each node and edge is explored in breadth-first order. |
| Worst | O(V^2) | O(V^2) | This implementation stores full path lists in the queue, so copying paths can become expensive in larger or deeper graphs. |

- The main reason the worst case grows is that each discovered path is copied as it is enqueued, which adds extra work beyond a parent-pointer-based BFS implementation.

## 7. Real-Life Use Cases
- Social networks: shortest connection distance for friend suggestions.
- Web crawling: discovering pages level by level from a seed URL.
- Puzzle solving: finding the minimum number of moves in an unweighted state graph.
- Networking: finding the smallest hop count between routers in a simple topology.

## 8. Comparison / When to Use vs Alternatives
| Approach | Use when | Notes |
|---|---|---|
| BFS shortest path | You need the fewest edges in an unweighted graph | Guarantees shortest hop count |
| DFS | You need to explore possible paths or solve backtracking problems | Does not guarantee the shortest path |
| Dijkstra | You need shortest paths in weighted graphs | More general, but more complex |

## 9. Common Mistakes / Gotchas
- Confusing BFS traversal with BFS shortest path; traversal returns visit order, not the path.
- Forgetting to mark nodes as visited before enqueueing them.
- Assuming BFS works for weighted graphs; it does not guarantee minimum total cost there.
- Using a list-based pop from the front instead of a queue can make the solution slower.

## 10. Code Reference
- [bfs_shorted_path.py](bfs_shorted_path.py)
- Implements shortest-path search by storing candidate paths in a queue and returning the first path that reaches the target.

## 11. Related Topics
- Graph traversal
- Shortest path algorithms
- Dijkstra's algorithm
- Unweighted graph problems

## 12. References
- CLRS, Introduction to Algorithms, Chapter 22
- Standard graph traversal notes from competitive-programming practice
