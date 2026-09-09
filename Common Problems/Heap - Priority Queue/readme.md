# Priority Queue / Heap — Interview Notes
 
## Core Concept
 
A **heap** is a complete binary tree stored as an array, satisfying the heap-order property:
 
- **Min-Heap**: parent ≤ children → smallest element at root
- **Max-Heap**: parent ≥ children → largest element at root
A **Priority Queue (PQ)** is the abstract data type; a **heap** is the standard concrete implementation (array-based, O(log n) insert/remove).
 
### Array Representation
For node at index `i` (0-indexed):
- Parent: `(i-1) / 2`
- Left child: `2i + 1`
- Right child: `2i + 2`
  
### Complexity Cheat Sheet
| Operation | Time |
|---|---|
| Peek (top) | O(1) |
| Insert (push) | O(log n) |
| Extract top (pop) | O(log n) |
| Build heap from array | O(n) |
| Heapify (sift-down/up) | O(log n) |
| Search arbitrary element | O(n) |