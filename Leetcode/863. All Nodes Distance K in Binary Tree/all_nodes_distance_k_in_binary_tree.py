# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_graph = {}
        child_graph ={}
        res = []
        def dfs(node, parent=None, distance = None):
            if not node:
                return False
            dist = distance+1 if distance is not None else None
            match = node==target
            if match:
                dist = 1
            
            if distance==k:
                res.append(node.val)
                
            left = dfs(node.left, node.val, dist)
            right = dfs(node.right, node.val, dist)
            any_match = left or right or match
            
            if any_match and root != node:
                parent_graph[node.val] = parent
            elif parent is not None and distance is None:
                child_graph.setdefault(parent, []).append(node.val)
                
            return any_match
        
        def read_nodes(val, distance):
            if distance==0:
                res.append(val)
                return
            if val in parent_graph:
                read_nodes(parent_graph[val], distance-1)
            for child in child_graph.get(val, []):
                read_nodes(child, distance-1)
        dfs(root)
        read_nodes(target.val, k)
        return res

def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


if __name__ == "__main__":
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert root is not None and root.left is not None
    print(Solution().distanceK(root, root.left, 2))

    root = build_tree([0, 2, 1, None, None, 3])
    assert root is not None and root.right is not None and root.right.left is not None
    print(Solution().distanceK(root, root.right.left, 3))