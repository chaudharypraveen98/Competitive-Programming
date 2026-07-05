# Dijkstra's Algorithm

## 1. Overview
- **What is it?** Dijkstra's Algorithm is a greedy shortest-path method used to find the minimum total distance from a source node to every reachable node in a graph with non-negative edge weights.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#shortest-path` `#greedy`

## 2. Problem It Solves
It solves the problem of finding the cheapest route between locations when each connection has a cost. A simple breadth-first search is not enough when some edges are more expensive than others.

## 3. Approach / Intuition
Think of it like expanding outward from the starting point while always picking the currently cheapest known frontier node.
- Initialize all distances as infinity except the start node, which gets distance 0.
- Use a min-heap to always process the node with the smallest known distance first.
- For each neighbor, compute the distance through the current node and update it if it is smaller.
- Repeat until every reachable node has been processed.

## 4. Pseudocode
```text
function dijkstra(graph, start):
    distances = map of all nodes to infinity
    distances[start] = 0
    heap = min-heap containing (0, start)

    while heap is not empty:
        current_distance, node = pop smallest entry from heap

        if current_distance is greater than distances[node]:
            continue

        for each neighbor, weight of node:
            new_distance = current_distance + weight
            if new_distance is smaller than distances[neighbor]:
                distances[neighbor] = new_distance
                push (new_distance, neighbor) into heap

    return distances
```

## 5. Assumptions & Constraints
- Assumes all edge weights are non-negative.
- Works for both directed and undirected graphs, depending on how edges are added.
- Returns the shortest distance from the start to every reachable vertex.
- Unreachable vertices remain at infinity.
- Does not handle graphs with negative weights correctly.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | The algorithm can stop early if the graph is very small or the heap is exhausted quickly. |
| Average | O((V + E) log V) | O(V + E) | Each edge is relaxed and each vertex is processed through a heap. |
| Worst | O((V + E) log V) | O(V + E) | The heap operations and edge relaxations dominate in dense or large graphs. |

- The worst case is driven by repeated heap insertions and extractions while relaxing edges across the graph.

## 7. Real-Life Use Cases
- GPS navigation systems: finding the lowest-cost route between two places.
- Network routing: choosing the cheapest path for data packets.
- Logistics planning: minimizing travel time or fuel cost across a map of destinations.
- Game AI: computing shortest movement cost through weighted terrain.

## 8. Comparison / When to Use vs Alternatives
| Approach | Use when | Notes |
|---|---|---|
| Dijkstra | You need shortest paths in graphs with non-negative weights | Greedy and efficient for this case |
| BFS shortest path | You need the fewest edges in an unweighted graph | Does not consider weights |
| Bellman-Ford | You need to support negative weights | More general but slower |

## 9. Common Mistakes / Gotchas
- Applying Dijkstra to graphs with negative edge weights.
- Forgetting the stale-entry check when using a heap.
- Confusing shortest distance with fewest edges; BFS is for the latter.
- Using the wrong data structure for the priority queue.

## 10. Code Reference
- [dijkstra_algorithm.py](dijkstra_algorithm.py)
- Implements Dijkstra's algorithm using a min-heap and edge relaxation to compute shortest distances.

## 11. Related Topics
- BFS shortest path
- Bellman-Ford algorithm
- Weighted graph problems
- Shortest path algorithms

## 12. References
- CLRS, Introduction to Algorithms, Chapter 24
- Standard shortest-path algorithm notes from competitive-programming practice
