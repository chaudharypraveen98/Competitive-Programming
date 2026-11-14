# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        self.path_exists = False
        def dfs(node, cur_sum=0):
            if not node:
                return False
            cur_sum+=node.val
            if not node.left and not node.right and cur_sum==targetSum:
                return True
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

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
        ([-2,None,-3],-5,True), 
        ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True)
    ]
    for values,target, expected in test_cases:
        result = Solution().hasPathSum(build_tree(values),target)
        assert result == expected, f"For {values}, expected {expected}, got {result}"
        print(f"Input: {values}\nOutput: {result}")
        