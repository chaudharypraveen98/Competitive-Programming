"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned ={}
        def dfs(start):
            temp_neighbours = []
            new_node = Node(start.val)
            cloned[start.val] = new_node
            for neighbour in start.neighbors:
              if neighbour.val in cloned:
                new_node.neighbors.append(cloned[neighbour.val]) 
              else:
                new_node.neighbors.append(dfs(neighbour))
            return new_node
        return dfs(node)

from collections import deque
from typing import List, Optional


class Node:

  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


# ==========================================
# Helper Functions to Build & Validate Graphs
# ==========================================


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
  """Constructs a Node-based graph from an adjacency list format."""
  if not adj_list:
    return None

  nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

  for i, neighbors in enumerate(adj_list):
    node_val = i + 1
    nodes[node_val].neighbors = [nodes[n_val] for n_val in neighbors]

  return nodes[1]


def is_deep_copy(original: Optional[Node], clone: Optional[Node]) -> bool:
  """Verifies that the cloned graph matches original structurally and in values,

  but consists of completely new Node instances in memory.
  """
  if not original and not clone:
    return True
  if not original or not clone:
    return False

  visited_orig = {}
  visited_clone = {}

  q_orig = deque([original])
  q_clone = deque([clone])

  visited_orig[original.val] = original
  visited_clone[clone.val] = clone

  while q_orig and q_clone:
    curr_orig = q_orig.popleft()
    curr_clone = q_clone.popleft()

    # 1. Values must match
    if curr_orig.val != curr_clone.val:
      print(
          f"Mismatch in node value: {curr_orig.val} vs {curr_clone.val}"
      )
      return False

    # 2. Must be distinct memory references
    if curr_orig is curr_clone:
      print(f"Node {curr_orig.val} was shallow copied (same reference)!")
      return False

    # 3. Neighbor count must match
    if len(curr_orig.neighbors) != len(curr_clone.neighbors):
      print(
          f"Neighbor count mismatch for Node {curr_orig.val}"
      )
      return False

    # Map neighbor values for structural verification
    clone_neighbors_map = {n.val: n for n in curr_clone.neighbors}

    for orig_neighbor in curr_orig.neighbors:
      # Check if corresponding neighbor exists in clone
      if orig_neighbor.val not in clone_neighbors_map:
        print(
            f"Node {curr_orig.val} missing cloned neighbor"
            f" {orig_neighbor.val}"
        )
        return False

      clone_neighbor = clone_neighbors_map[orig_neighbor.val]

      # Check memory reference separation for neighbors
      if orig_neighbor is clone_neighbor:
        print(
            f"Neighbor {orig_neighbor.val} was shallow copied!"
        )
        return False

      # Traverse unvisited nodes
      if orig_neighbor.val not in visited_orig:
        visited_orig[orig_neighbor.val] = orig_neighbor
        visited_clone[clone_neighbor.val] = clone_neighbor
        q_orig.append(orig_neighbor)
        q_clone.append(clone_neighbor)

  return len(q_orig) == 0 and len(q_clone) == 0


# ==========================================
# Solution Class
# ==========================================


class Solution:

  def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
    if not node:
      return None

    cloned = {}

    def dfs(curr: Node) -> Node:
      if curr in cloned:
        return cloned[curr]

      copy = Node(curr.val)
      cloned[curr] = copy

      for neighbor in curr.neighbors:
        copy.neighbors.append(dfs(neighbor))

      return copy

    return dfs(node)


# ==========================================
# Test Suite Execution
# ==========================================

test_cases = [
    {
        "name": "Standard 4-node Graph (LeetCode Ex 1)",
        "adj_list": [[2, 4], [1, 3], [2, 4], [1, 3]],
    },
    {
        "name": "Single Node with No Neighbors (LeetCode Ex 2)",
        "adj_list": [[]],
    },
    {"name": "Empty Graph (LeetCode Ex 3)", "adj_list": []},
    {
        "name": "Line / Path Graph (1 - 2 - 3 - 4)",
        "adj_list": [[2], [1, 3], [2, 4], [3]],
    },
    {"name": "Triangle / Simple Cycle (1 - 2 - 3 - 1)", "adj_list": [[2, 3], [1, 3], [1, 2]]},
    {
        "name": "Complete Graph K4 (Fully Connected)",
        "adj_list": [
            [2, 3, 4],
            [1, 3, 4],
            [1, 2, 4],
            [1, 2, 3],
        ],
    },
    {
        "name": "Star Graph (Node 1 connected to 2, 3, 4)",
        "adj_list": [[2, 3, 4], [1], [1], [1]],
    },
]

sol = Solution()

print("--- Running Clone Graph Test Cases ---\n")
for i, test in enumerate(test_cases, 1):
  graph_input = build_graph(test["adj_list"])
  cloned_graph = sol.cloneGraph(graph_input)

  passed = is_deep_copy(graph_input, cloned_graph)
  status = "PASSED" if passed else "FAILED"

  print(f"Test {i}: {test['name']} -> [{status}]")

print("\nAll tests completed.")