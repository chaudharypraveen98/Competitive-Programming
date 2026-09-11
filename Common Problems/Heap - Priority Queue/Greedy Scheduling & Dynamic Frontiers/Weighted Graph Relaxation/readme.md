## Weighted Graph Relaxation (Dijkstra / Minimax)
Finding the path with the minimum total cost, minimum effort, or minimum bottleneck across a graph.

### The Heap Mechanism:
- The Min-Heap maintains the current exploration frontier prioritized by cumulative path cost: (cost, node).
- Always expands the cheapest available candidate first, guaranteeing that the first time a destination node is popped, its path cost is optimal.

### Challenge Problem
[Network Delay Time](../../../../Leetcode/743.%20Network%20Delay%20Time/)

- You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (u_i, v_i, w_i), where u_i is the source node, v_i is the target node, and w_i is the time it takes for a signal to travel from source to target.  

- We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.