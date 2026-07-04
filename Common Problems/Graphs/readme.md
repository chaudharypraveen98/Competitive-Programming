# Graphs

## 1. What is a Graph?
A graph `G = (V, E)` is a set of **vertices (nodes)** connected by **edges**.

- **Directed** vs **Undirected**
- **Weighted** vs **Unweighted**
- **Cyclic** vs **Acyclic** (DAG = Directed Acyclic Graph)
- **Connected** vs **Disconnected**
- **Sparse** (few edges) vs **Dense** (many edges)

---

## 2. Representations

### a) Adjacency List (most common)
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```
- Space: `O(V + E)`
- Good for sparse graphs, fast neighbor iteration.

Using `defaultdict`:
```python
from collections import defaultdict

graph = defaultdict(list)
edges = [('A','B'), ('B','C'), ('A','C')]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)   # omit this line if directed
```

### b) Adjacency Matrix
```python
n = 5
matrix = [[0]*n for _ in range(n)]
matrix[0][1] = 1   # edge from 0 to 1
```
- Space: `O(V^2)`
- Good for dense graphs, O(1) edge lookup.
- Wasteful for sparse graphs.

### c) Edge List
```python
edges = [(0,1), (1,2), (2,0)]
```
- Simple, used in algorithms like Kruskal's MST.

### d) Weighted Graph (adjacency list with weights)
```python
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('D', 2)],
    'C': [('A', 1), ('D', 5)],
    'D': [('B', 2), ('C', 5)]
}
```

---

## 3. Graph Traversals

### a) Breadth-First Search (BFS)
- Uses a **queue**. Explores level by level. Good for shortest path in **unweighted** graphs.

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```
- Time: `O(V + E)`

### b) Depth-First Search (DFS)
- Uses a **stack** (or recursion). Explores as deep as possible first.

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return order
```
- Time: `O(V + E)`

---

## 4. Shortest Path Algorithms

### a) BFS Shortest Path (unweighted)
```python
def shortest_path_bfs(graph, start, target):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == target:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None
```

### b) Dijkstra's Algorithm (weighted, no negative edges)
```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist
```
- Time: `O((V + E) log V)` with a heap.

### c) Bellman-Ford (handles negative weights)
```python
def bellman_ford(vertices, edges, start):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Optional: check for negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Negative weight cycle detected")
    return dist
```
- Time: `O(V·E)`

### d) Floyd-Warshall (all-pairs shortest path)
```python
def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```
- Time: `O(V^3)`

---

## 5. Cycle Detection

### a) Undirected Graph (using DFS)
```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

### b) Directed Graph (using colors / recursion stack)
```python
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    return any(color[node] == WHITE and dfs(node) for node in graph)
```

---

## 6. Topological Sort (DAGs only)

### a) DFS-based
```python
def topo_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]
```

### b) Kahn's Algorithm (BFS-based, using in-degree)
```python
def topo_sort_kahn(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(order) != len(graph):
        raise ValueError("Graph has a cycle")
    return order
```

---

## 7. Minimum Spanning Tree (MST)

### a) Kruskal's Algorithm (Union-Find based)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda e: e[2])   # sort by weight
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    for u, v, w in edges:
        if uf.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))
    return mst_weight, mst_edges
```
- Time: `O(E log E)`

### b) Prim's Algorithm (heap-based)
```python
def prim(graph, start):
    visited = {start}
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    mst_weight = 0
    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst_weight += w
            for to, weight in graph[v]:
                if to not in visited:
                    heapq.heappush(edges, (weight, v, to))
    return mst_weight
```
- Time: `O(E log V)`

---

## 8. Connected Components

```python
def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, comp):
        visited.add(node)
        comp.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, comp)

    for node in graph:
        if node not in visited:
            comp = []
            dfs(node, comp)
            components.append(comp)
    return components
```

For **directed** graphs → use **Kosaraju's** or **Tarjan's** algorithm for Strongly Connected Components (SCCs).

---

## 9. Common Interview Patterns

| Pattern | Use Case |
|---|---|
| BFS | Shortest path (unweighted), level-order problems |
| DFS | Path existence, backtracking, cycle detection |
| Union-Find | Connectivity, cycle detection, Kruskal's MST |
| Topological Sort | Task scheduling, dependency resolution |
| Dijkstra | Shortest path with positive weights |
| Bellman-Ford | Shortest path with negative weights |
| Floyd-Warshall | All-pairs shortest paths, small graphs |
| Bitmask + BFS/DFS | Traveling Salesman-type problems |
| Multi-source BFS | "Rotting oranges", nearest facility problems |

---

## 10. Time Complexity Cheat Sheet

| Algorithm | Time | Space |
|---|---|---|
| BFS / DFS | O(V + E) | O(V) |
| Dijkstra (heap) | O((V+E) log V) | O(V) |
| Bellman-Ford | O(V·E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Kruskal's MST | O(E log E) | O(V) |
| Prim's MST | O(E log V) | O(V) |
| Topological Sort | O(V + E) | O(V) |
| Union-Find (path compression + rank) | ~O(α(n)) per op | O(V) |

---

## 11. Quick Tips for Exams/Interviews
- Always clarify: **directed or undirected? weighted? cyclic possible?**
- Adjacency list is default choice unless graph is dense or you need O(1) edge checks.
- BFS → shortest path in unweighted graphs. DFS → exploring all paths / backtracking.
- Cycle in undirected → track parent. Cycle in directed → track recursion stack (colors).
- Union-Find is your best friend for "are these connected" or "will adding this edge form a cycle" questions.
- For grid-based problems (matrix as graph), treat each cell as a node; use BFS/DFS with 4 or 8 directional moves.