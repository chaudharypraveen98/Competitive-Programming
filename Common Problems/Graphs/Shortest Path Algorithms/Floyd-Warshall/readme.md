# Floyd-Warshall Algorithm

## 1. Overview
- **What is it?** Floyd-Warshall finds the shortest path between every pair of vertices in a weighted graph by gradually considering more possible intermediate stops.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#shortest-path` `#dynamic-programming`

## 2. Problem It Solves
It solves the all-pairs shortest path problem, which is useful when you need the minimum-cost route between any two nodes instead of only from one starting node.

## 3. Approach / Intuition
Think of it as expanding the set of allowed intermediate locations one vertex at a time.
- Start with the direct edge weights already known in the matrix.
- For each possible intermediate vertex $k$, check whether going from $i$ to $k$ to $j$ is shorter than the current best path from $i$ to $j$.
- Update the distance matrix whenever a shorter route is found.
- Continue until every vertex has been tried as an intermediate stop.

## 4. Pseudocode
```text
function floyd_warshall(graph):
    dist = copy of graph matrix
    for each vertex k:
        for each vertex i:
            for each vertex j:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```

## 5. Assumptions & Constraints
- Assumes the graph is represented as a distance matrix.
- Works for both directed and undirected graphs.
- Supports negative edge weights, but it does not handle negative cycles.
- Distance from a vertex to itself is always $0$.
- Unreachable pairs remain as infinity.
- This implementation returns the shortest distances, not the actual path reconstruction.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | $O(V^3)$ | $O(V^2)$ | The algorithm still checks all possible triples of vertices |
| Average | $O(V^3)$ | $O(V^2)$ | Same because the nested loops always run to completion |
| Worst | $O(V^3)$ | $O(V^2)$ | Dense graphs still require the full triple loop |

The main cost comes from the three nested loops, so the runtime grows cubically with the number of vertices.

## 7. Real-Life Use Cases
- Airline route planning: cheapest connection between any two airports.
- Network design: best routing cost between multiple servers.
- Robotics and map systems: minimum travel cost between many locations.
- Transportation planning: shortest path between all city pairs in a weighted network.

## 8. Comparison / When to Use vs Alternatives
- Compared with Dijkstra: use Dijkstra when you only need the shortest path from one source node.
- Compared with Bellman-Ford: use Bellman-Ford when you need one-source shortest paths and want to handle negative edges more explicitly.
- Compared with both: use Floyd-Warshall when you need all-pairs shortest paths and the graph size is manageable.

## 9. Common Mistakes / Gotchas
- Using the wrong loop order; the intermediate vertex $k$ must be the outermost loop.
- Forgetting to initialize the matrix with the correct direct edge values.
- Treating infinity values as real distances.
- Allowing negative cycles, which make shortest paths undefined.

## 10. Code Reference
- [floyd_warshall.py](floyd_warshall.py)
- Implements the algorithm using a matrix-based graph representation and returns a dictionary of shortest distances.

## 11. Related Topics
- Dijkstra
- Bellman-Ford
- Shortest path in DAGs

## 12. References (optional)
- CLRS, Introduction to Algorithms
- Standard all-pairs shortest path discussion
