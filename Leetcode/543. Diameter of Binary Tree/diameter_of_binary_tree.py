# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def get_height(node):
            if not node:
                return -1  # Height of None is -1 in terms of edges
                
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # The diameter passing through the current node is the number of edges 
            # in the left path + right path + 2 edges connecting to left & right children
            self.max_diameter = max(self.max_diameter, left_height + right_height + 2)
            
            # Return the maximum height of the current node
            return max(left_height, right_height) + 1

        get_height(root)
        return self.max_diameter


def build_tree(values: list[int | None]) -> Optional[TreeNode]:
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
    test_cases = [
        ([1, 2, 3], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1], 0),
        ([], 0),
    ]

    for values, expected in test_cases:
        root = build_tree(values)
        result = Solution().diameterOfBinaryTree(root)
        print(f"Tree: {values} -> diameter = {result} | expected = {expected}")