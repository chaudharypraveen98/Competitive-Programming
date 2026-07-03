## Adjacency Matrix

```
n = 5
matrix = [[0]*n for _ in range(n)]
matrix[0][1] = 1   # edge from 0 to 1
```

- Space: O(V^2)
- Good for dense graphs, O(1) edge lookup.
- Wasteful for sparse graphs.