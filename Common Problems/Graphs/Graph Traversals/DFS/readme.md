# Depth-First Search (DFS)

## 1. Overview
- **What is it?** DFS explores a graph by going as deep as possible along one branch before backtracking and trying another path. It is commonly used for traversal, cycle detection, and exploring connected components.
- **Category:** Graph
- **Level:** Beginner
- **Tags:** `#graph` `#traversal`

## 2. Problem It Solves
It helps answer questions such as “can I reach this node?” or “what nodes are reachable from a starting point?” when you want to explore a path fully before moving to the next option.

## 3. Approach / Intuition
Think of it like walking through a maze while keeping track of the path you are on.
- Start from the given node and mark it visited.
- Follow one neighbor, keep going deeper until you cannot continue.
- When you hit a dead end, backtrack and try the next neighbor.
- Continue until all reachable nodes have been explored.

## 4. Pseudocode
```text
function dfs(graph, start):
    create empty stack
    create empty visited set
    create empty order list

    push start onto stack
    while stack is not empty:
        node = pop from top of stack
        if node not in visited:
            add node to visited
            add node to order
            for each neighbor in graph.adjacent_list[node]:
                if neighbor not in visited:
                    push neighbor onto stack
    return order
```

## 5. Assumptions & Constraints
- Assumes the graph is represented using an adjacency list.
- Works for both directed and undirected graphs in the provided implementation.
- Handles disconnected graphs by traversing only the component reachable from the start node.
- The implementation in this folder includes both iterative and recursive forms.

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | Each node and edge is processed once. |
| Average | O(V + E) | O(V) | The same bound applies for typical graph shapes. |
| Worst | O(V + E) | O(V) | Even in a dense graph, the algorithm still visits every node and edge once. |

The worst case occurs when the graph is large or dense, but the total work remains proportional to the number of vertices and edges.

## 7. Real-Life Use Cases
- Web crawlers: exploring a site graph by following links deeply.
- Maze and puzzle solvers: exploring one path fully before trying alternatives.
- Dependency and call graph analysis: finding reachable components in a structure.

## 8. Comparison / When to Use vs Alternatives
- Use DFS when you want to explore deeply before branching out.
- Use BFS when you need shortest paths in an unweighted graph.
- Use topological sort or dynamic programming when the problem has additional structure, such as ordering or optimization constraints.

## 9. Common Mistakes / Gotchas
- Forgetting to mark a node as visited before pushing its neighbors.
- Causing infinite recursion in recursive DFS when cycles are not handled properly.
- Depending on the neighbor order, the traversal order can vary even though the set of visited nodes remains correct.

## 10. Code Reference
- [dfs.py](dfs.py) — implements iterative DFS with a stack and also includes a recursive DFS variant.

## 11. Related Topics
- [BFS](../BFS/readme.md)

## 12. References (optional)
- CLRS, Introduction to Algorithms, Chapter 22.
