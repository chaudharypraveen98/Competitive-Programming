# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:

        def dfs(node):
            if not node:
                return (0,0)
            
            left_skip, left_include = dfs(node.left)
            right_skip, right_include = dfs(node.right)
            root_include = node.val + left_skip + right_skip
            dont_include = max(left_skip, left_include)+ max(right_skip, right_include)
            return (dont_include, root_include)
        
        return max(dfs(root))
    
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
        # ([3,2,3,None,3,None,1], 7),
        # ([3,4,5,1,3,None,1], 9),
        ([4,1,None,2,None,3], 7)
    ]
    for values, expected in test_cases:
        result = Solution().rob(build_tree(values))
        assert result == expected, f"For {values}, expected {expected}, got {result}"
        print(f"Input: {values}\nOutput: {result}")
        