# Breadth-First Search (BFS)

## 1. Overview
- **What is it?** BFS explores a graph level by level, visiting all neighbors of a node before moving deeper. It is commonly used to traverse connected components and find shortest paths in unweighted graphs.
- **Category:** Graph
- **Level:** Beginner
- **Tags:** `#graph` `#traversal` `#shortest-path`

## 2. Problem It Solves
It helps answer questions like “what nodes are reachable from here?” or “what is the shortest number of steps from start to each node?” in an unweighted graph.

## 3. Approach / Intuition
Think of it like ripples spreading outward from a starting point.
- Start from the given node, mark it visited, and place it in a queue.
- Repeatedly remove the front node from the queue and process it.
- Visit each unvisited neighbor, mark it visited, and add it to the queue.
- Continue until every reachable node has been processed.

## 4. Pseudocode
```text
function bfs(graph, start):
    create empty queue
    create empty visited set
    create empty order list

    add start to queue and visited
    while queue is not empty:
        node = remove first element from queue
        append node to order
        for each neighbor in graph.adjacent_list[node]:
            if neighbor not in visited:
                add neighbor to visited
                add neighbor to queue
    return order
```

## 5. Assumptions & Constraints
- Assumes the graph is represented using an adjacency list.
- Works for both directed and undirected graphs in the provided implementation.
- Handles disconnected graphs by traversing only the component reachable from the start node.
- Does not reconstruct the actual path; it returns the traversal order.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | Each node and edge is processed once. |
| Average | O(V + E) | O(V) | The same bound applies for typical graph shapes. |
| Worst | O(V + E) | O(V) | Even in a dense graph, the algorithm still visits every node and edge once. |

The worst case occurs when the graph is large or dense, but the total work remains proportional to the number of vertices and edges.

## 7. Real-Life Use Cases
- Social networks: exploring friend-of-friend connections by distance.
- Web crawlers: discovering pages level by level from a seed URL.
- Puzzle solvers: finding the shortest sequence of moves in unweighted state spaces.

## 8. Comparison / When to Use vs Alternatives
- Use BFS when you need the shortest path in an unweighted graph.
- Use DFS when you want exhaustive search, backtracking, or path exploration without distance concerns.
- Use Dijkstra when edge weights are not uniform.

## 9. Common Mistakes / Gotchas
- Marking a node visited only when it is popped from the queue rather than when it is enqueued.
- Using a list with pop(0) instead of a deque, which makes each dequeue slower.
- Forgetting to mark the starting node as visited before the loop begins.

## 10. Code Reference
- [bfs.py](bfs.py) — implements iterative BFS using a queue and a visited set, with support for directed and undirected graphs.

## 11. Related Topics
- [DFS](../DFS/readme.md)

## 12. References (optional)
- CLRS, Introduction to Algorithms, Chapter 22.
