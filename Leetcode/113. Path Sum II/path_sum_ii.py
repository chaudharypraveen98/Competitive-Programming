# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, path, curSum):
            if not node: return
            curSum += node.val
            path.append(node.val)
            if not node.left and not node.right and curSum == targetSum:
                res.append(path[:])
            dfs(node.left, path, curSum)
            dfs(node.right, path, curSum)
            path.pop()
        dfs(root, [], 0)
        return res
        
    
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
        ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22, [[5,4,11,2],[5,8,4,5]])
    ]
    for values,target, expected in test_cases:
        result = Solution().pathSum(build_tree(values),target)
        assert result == expected, f"For {values}, expected {expected}, got {result}"
        print(f"Input: {values}\nOutput: {result}")
        