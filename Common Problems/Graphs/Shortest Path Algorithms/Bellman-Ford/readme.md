# Bellman-Ford Algorithm

## 1. Overview
- **What is it?** Bellman-Ford is a shortest-path algorithm that finds the minimum distance from one source node to every reachable node in a graph, even when some edges have negative weights.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#shortest-path` `#cycle-detection`

## 2. Problem It Solves
It solves the problem of finding the cheapest route in a weighted graph when edge costs may be negative. Standard greedy methods such as Dijkstra are not reliable in that case because they can fail if a negative-weight edge appears before a better path is discovered.

## 3. Approach / Intuition
Think of it like repeatedly relaxing every road connection and checking whether a better route becomes available.
- Start with a distance of 0 for the source and infinity for all other vertices.
- Relax every edge once per round, updating a destination if a cheaper path is found through the current source.
- Repeat this process for $V - 1$ rounds, where $V$ is the number of vertices.
- If any edge can still be improved after the final round, then a negative-weight cycle is reachable from the source.

## 4. Pseudocode
```text
function bellman_ford(graph, start):
    distances = map of every vertex to infinity
    distances[start] = 0

    repeat V - 1 times:
        for each edge (u, v, weight) in graph:
            if distances[u] is finite and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for each edge (u, v, weight) in graph:
        if distances[u] is finite and distances[u] + weight < distances[v]:
            raise error "Negative weight cycle detected"

    return distances
```

## 5. Assumptions & Constraints
- Assumes the graph is represented as an edge list, where each edge is stored as a triple of source, destination, and weight.
- Works for directed and undirected graphs depending on how edges are added.
- Supports negative edge weights, but not negative-weight cycles reachable from the source.
- Unreachable vertices remain at infinity.
- Requires the start vertex to exist in the graph.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(VE) | O(V) | The algorithm still performs the full relaxation rounds, so the cost does not improve much for easier inputs. |
| Average | O(VE) | O(V) | Each of the $V - 1$ rounds scans all $E$ edges. |
| Worst | O(VE) | O(V) | Dense graphs with many edges make the repeated edge relaxations the dominant cost. |

- The worst case is driven by the need to relax every edge $V - 1$ times, so the runtime grows in proportion to the number of vertices multiplied by the number of edges.

## 7. Real-Life Use Cases
- Finance: detecting arbitrage opportunities in currency exchange networks where one path can produce a net gain.
- Project scheduling: finding the lowest-cost path in dependency graphs when some tasks create a reward rather than a cost.
- Routing systems: evaluating routes when certain links have discounts, penalties, or negative adjustments.
- Supply chain planning: modeling cost changes where a transition can reduce total expense under certain conditions.

## 8. Comparison / When to Use vs Alternatives
| Approach | Use when | Notes |
|---|---|---|
| Bellman-Ford | You need shortest paths and negative edge weights are possible | Correct but slower than Dijkstra |
| Dijkstra | You need shortest paths in graphs with non-negative weights | Faster because it uses a priority queue |
| Floyd-Warshall | You need all-pairs shortest paths | Works for all pairs, but is more expensive for single-source problems |

## 9. Common Mistakes / Gotchas
- Forgetting to run the extra validation pass after the main relaxation rounds.
- Assuming Bellman-Ford can handle negative cycles without raising an error.
- Using the wrong graph representation; this implementation is designed for an edge-list graph rather than an adjacency list.
- Treating unreachable vertices as zero instead of infinity.

## 10. Code Reference
- [bellman_ford.py](bellman_ford.py)
- Implements the standard single-source Bellman-Ford approach using repeated edge relaxation and negative-cycle detection.

## 11. Related Topics
- [Dijkstra's Algorithm](../Dijkstra's%20Algorithm/readme.md)
- [Floyd-Warshall](../Floyd-Warshall/readme.md)
- Shortest path algorithms
- Graph cycle detection

## 12. References
- CLRS, Introduction to Algorithms, Chapter 24
- Standard shortest-path notes from competitive-programming practice
