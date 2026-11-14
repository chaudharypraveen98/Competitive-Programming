# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, path=''):
            if not node: return 0
            path += str(node.val)
            if not node.left and not node.right:
                return int(path)
            return dfs(node.left, path) + dfs(node.right, path)
            
        return dfs(root)
        
    
def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if values[index] is not None:
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
        ([4,9,0,5,1], 1026)
    ]
    for values, expected in test_cases:
        result = Solution().sumNumbers(build_tree(values))
        assert result == expected, f"For {values}, expected {expected}, got {result}"
        print(f"Input: {values}\nOutput: {result}")
        