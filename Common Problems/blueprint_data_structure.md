# DSA Repo Documentation Blueprint

This is the standard template used to auto-generate a `README.md` (or `NOTES.md`) for every algorithm/data-structure file in this repository. An AI agent should read the source code file and fill out this exact structure — same sections, same order, every time — so the whole repo stays consistent and revision-friendly.

Not all the sections are mandatory and necessary, use only which you find helpful

---

## How to use this blueprint (instructions for the AI agent)

1. Read the target source file fully before writing anything.
2. Fill every section below — do not skip a section; write "N/A" only if truly not applicable, and justify why in one line.
3. Keep language simple and revision-friendly — written for future-you skimming this a year later, not for a first-time learner.
4. Pseudocode must be language-agnostic (no Python-specific syntax like list comprehensions) even if the source code is in Python.
5. Time/space complexity must include **best, average, and worst case** where they differ meaningfully.
6. Output file name convention: place it next to the source file as `README.md` inside that topic's folder, e.g. `graphs/bfs/README.md`.
7. Tags and Level must come from the controlled vocabularies given in this blueprint (Section: Controlled Vocabularies) — do not invent new tags without adding them to the vocabulary list first.

---

## Template to fill in for each file

```markdown
# <Algorithm / Data Structure Name>

## 1. Overview
- **What is it?** 2-4 sentences, plain language, no jargon dump.
- **Category:** (e.g. Graph Traversal, Sorting, Tree, Hashing, Dynamic Programming, Greedy, Backtracking)
- **Level:** Beginner | Intermediate | Advanced
- **Tags:** `#tag1` `#tag2` `#tag3` (see Controlled Vocabulary below)

## 2. Problem It Solves
- What real problem motivated this? What breaks or becomes inefficient without it?
- 1-2 sentences max.

## 3. Approach / Intuition
- Explain the core idea in plain English before any code or pseudocode.
- Use an analogy if one exists (e.g. BFS = ripples in a pond, DFS = maze-solving with a piece of string).
- Bullet the key steps at a high level (3-6 bullets).

## 4. Pseudocode
Language-agnostic, numbered steps or code-block pseudocode. Example style:

\`\`\`
function bfs(graph, start):
    create empty queue, empty visited set, empty order list
    add start to queue and visited
    while queue is not empty:
        node = remove from front of queue
        add node to order
        for each neighbor of node:
            if neighbor not in visited:
                mark neighbor visited
                add neighbor to queue
    return order
\`\`\`

## 5. Assumptions & Constraints
- Input assumptions (e.g. "graph has no negative weights", "array is 0-indexed", "no duplicate nodes")
- Edge cases explicitly handled (empty input, single node, disconnected graph, self-loops, cycles)
- Edge cases explicitly NOT handled (call these out honestly — don't hide gaps)

## 6. Complexity Analysis
| Case | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Best | | | |
| Average | | | |
| Worst | | | |

- Explain *why* — one sentence justifying the worst case in particular (what input causes it).

## 7. Real-Life Use Cases
- 2-4 concrete, named examples (e.g. "BFS → shortest hop count in social network friend suggestions", "Dijkstra → GPS navigation route cost").
- Avoid vague answers like "used in networking" — name the actual product/system pattern.

## 8. Comparison / When to Use vs Alternatives
- Brief table or bullets: this vs. the 1-2 closest alternative approaches, and when to pick which.
- Example: BFS vs DFS — BFS for shortest path in unweighted graphs, DFS for exhaustive search/backtracking.

## 9. Common Mistakes / Gotchas
- Bugs people commonly introduce (e.g. mutable default arguments, forgetting visited-on-push vs visited-on-pop, off-by-one errors).
- Pull these from actual code review if possible, not generic filler.

## 10. Code Reference
- Link/path to the source file in this repo: `path/to/file.py`
- One-line note on what's implemented (recursive vs iterative, directed vs undirected support, etc.)

## 11. Related Topics
- Cross-links to other README files in this repo that build on or relate to this one.
- Example: "See also: [Topological Sort](../topo-sort/README.md), [Union-Find](../union-find/README.md)"

## 12. References (optional)
- Any external resource used to verify correctness (docs, papers, textbook chapter) — not required, but good practice for non-trivial algorithms.
```

---

## Controlled Vocabularies

### Level (pick exactly one)
- `Beginner` — no prerequisites beyond basic loops/recursion
- `Intermediate` — assumes traversal/basic structures already known
- `Advanced` — assumes multiple prior topics as prerequisites (e.g. requires knowing both BFS and Union-Find)

### Tags (reuse existing tags before creating new ones)
`#array` `#string` `#linked-list` `#stack` `#queue` `#tree` `#binary-tree` `#bst` `#heap` `#graph` `#hashing` `#trie`
`#sorting` `#searching` `#recursion` `#backtracking` `#dynamic-programming` `#greedy` `#divide-and-conquer`
`#two-pointers` `#sliding-window` `#union-find` `#bit-manipulation` `#math`
`#traversal` `#shortest-path` `#mst` `#topological-sort` `#cycle-detection`

### Category (top-level folder grouping — pick exactly one)
`Array` `String` `Linked List` `Stack` `Queue` `Tree` `Graph` `Hashing` `Sorting` `Searching`
`Dynamic Programming` `Greedy` `Backtracking` `Bit Manipulation` `Math`

---

## Filled Example (reference — do not copy verbatim, use as a quality bar)

```markdown
# Breadth-First Search (BFS)

## 1. Overview
- **What is it?** A graph traversal algorithm that explores all neighbors of a node before
  moving to the next level, using a queue to process nodes in the order they were discovered.
- **Category:** Graph
- **Level:** Beginner
- **Tags:** `#graph` `#traversal` `#shortest-path`

## 2. Problem It Solves
Finding the shortest path (in terms of edge count) between two nodes in an unweighted graph,
or visiting all nodes level by level.

## 3. Approach / Intuition
Think of it like ripples spreading in a pond — you visit everything one step away from the
start before anything two steps away.
- Start at the source node, mark it visited, add it to a queue.
- Repeatedly pop the front of the queue, process it, and enqueue all its unvisited neighbors.
- Continue until the queue is empty.

## 4. Pseudocode
\`\`\`
function bfs(graph, start):
    queue = [start]
    visited = {start}
    order = []
    while queue is not empty:
        node = dequeue from front
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                enqueue neighbor
    return order
\`\`\`

## 5. Assumptions & Constraints
- Assumes the graph is represented as an adjacency list.
- Handles disconnected graphs (only traverses the component reachable from `start`).
- Does NOT return shortest path *nodes* — only visit order. Use parent-tracking for actual path reconstruction.

## 6. Complexity Analysis
| Case | Time | Space | Notes |
|---|---|---|---|
| Best | O(V + E) | O(V) | Every node/edge visited once regardless of graph shape |
| Average | O(V + E) | O(V) | Same — BFS complexity doesn't vary by input shape |
| Worst | O(V + E) | O(V) | Dense graph (E ≈ V²) still linear in V+E, just larger constant |

## 7. Real-Life Use Cases
- Social networks: "people you may know" (friends-of-friends, shortest connection distance)
- GPS/maps: shortest route by number of hops when all roads are equal weight
- Web crawlers: level-by-level page discovery from a seed URL
- Puzzle solvers: shortest sequence of moves (e.g. word ladder, sliding puzzle)

## 8. Comparison / When to Use vs Alternatives
| | BFS | DFS |
|---|---|---|
| Use when | Shortest path in unweighted graph | Exhaustive search, backtracking, cycle detection |
| Memory pattern | Wide (queue can hold many nodes at once) | Deep (stack holds one path at a time) |

## 9. Common Mistakes / Gotchas
- Marking visited on *pop* instead of *push* — causes duplicate enqueues (still correct, but wasteful).
- Using a list with `.pop(0)` instead of `deque.popleft()` — degrades to O(n) per dequeue.
- Forgetting to mark the start node visited before the loop begins.

## 10. Code Reference
- `graphs/bfs/bfs.py`
- Implements iterative BFS using `collections.deque`, supports directed and undirected graphs.

## 11. Related Topics
- See also: [DFS](../dfs/README.md), [Shortest Path — Dijkstra](../dijkstra/README.md)

## 12. References
- CLRS, Introduction to Algorithms, Chapter 22.
```

---

## Repo-Level Index (optional, generate once at repo root)

In addition to per-topic READMEs, maintain one root-level `INDEX.md` that lists every topic with its Level and Tags, so the whole repo is scannable at a glance:

```markdown
| Topic | Category | Level | Tags | Path |
|---|---|---|---|---|
| BFS | Graph | Beginner | #graph #traversal | graphs/bfs/ |
| DFS | Graph | Beginner | #graph #traversal | graphs/dfs/ |
| Dijkstra | Graph | Intermediate | #graph #shortest-path | graphs/dijkstra/ |
```

Regenerate/update this index row whenever a new topic README is added.
