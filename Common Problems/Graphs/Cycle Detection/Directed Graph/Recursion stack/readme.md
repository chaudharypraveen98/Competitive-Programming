# Cycle Detection in a Directed Graph (Using Recursion Stack)

## 1. Overview
- **What is it?** This is a graph algorithm that checks whether a directed graph contains a cycle by tracking nodes currently being explored in the depth-first search path.
- **Category:** Graph
- **Level:** Intermediate
- **Tags:** `#graph` `#cycle-detection` `#recursion` `#traversal`

## 2. Problem It Solves
A directed graph can contain loops such as A → B → C → A. Without cycle detection, algorithms like topological sort may behave incorrectly or fail to produce a valid order.

## 3. Approach / Intuition
Think of DFS as walking through a maze while keeping a trail of where you have stepped. If you reach a node that is already on the current trail, you have found a cycle.
- Start DFS from each unvisited node.
- Mark the node as "currently visiting" while exploring its neighbors.
- If a neighbor is already on the current recursion path, return True.
- If a node finishes exploring, mark it as fully processed.
- Repeat for all disconnected components.

## 4. Pseudocode
```text
function has_cycle_directed(graph):
    visited = empty set
    for each node in graph:
        if node not in visited and dfs(node, visited, empty set):
            return True
    return False

function dfs(node, visited, recursion_stack):
    add node to visited
    add node to recursion_stack

    for each neighbor in graph[node]:
        if neighbor in recursion_stack:
            return True
        if neighbor not in visited and dfs(neighbor, visited, recursion_stack):
            return True

    remove node from recursion_stack
    return False
```

## 5. Assumptions & Constraints
- Assumes the graph is stored as an adjacency list.
- Works for directed graphs only; the rule for undirected graphs is different because edges can be traversed backward.
- Handles disconnected graphs by checking each component separately.
- Handles self-loops, such as A → A, as a cycle.
- Does not return the actual cycle path, only whether a cycle exists.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | Each node and edge may be checked once in a simple acyclic graph |
| Average | O(V + E) | O(V) | DFS explores each node and edge once |
| Worst | O(V + E) | O(V) | A dense directed graph still costs linear work in terms of total vertices and edges |

- The worst case happens when the graph is large and every node has many outgoing edges, but the algorithm still processes each edge at most once during the DFS traversal.

## 7. Real-Life Use Cases
- Dependency management: detecting circular dependencies in build systems or package graphs.
- Task scheduling: finding whether a set of tasks depends on itself indirectly.
- Compiler design: checking for circular references in parse or dependency graphs.

## 8. Comparison / When to Use vs Alternatives
- Use this when you need to detect cycles in a directed graph quickly.
- Compared with an undirected cycle check, this version uses a recursion stack because a back-edge in a directed graph means "ancestor on the current path", not simply "parent".
- Compared with topological sort, this is simpler when the only question is whether a cycle exists.

## 9. Common Mistakes / Gotchas
- Forgetting to remove a node from the recursion stack after finishing its DFS branch.
- Using parent tracking from undirected graphs in a directed graph, which does not capture the same idea.
- Missing disconnected components by only checking one starting node.
- Confusing visited with recursion-stack state; a node can be visited but not currently active in the DFS path.

## 10. Code Reference
- `recursion_stack.py`
- Implements cycle detection for directed graphs using DFS with a recursion stack and a visited set.

## 11. Related Topics
- See also: [Graphs overview](../../../readme.md)
- Related patterns: topological sort, DFS traversal, and cycle detection in undirected graphs.

## 12. References
- CLRS, Introduction to Algorithms, Chapter on graph traversal and DFS.
- Standard graph theory notes on depth-first search and cycle detection.
