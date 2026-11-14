# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        self.numOfPaths = 0

        def test(node, target):
            # exit condition
            if node is None:
                return
            if node.val == target:
                self.numOfPaths += 1
                
            # test break down
            test(node.left, target-node.val)
            test(node.right, target-node.val)

        def dfs(node, target):
            if not node:
                return 
            test(node, target)
            dfs(node.left, target) 
            dfs(node.right, target) 
        dfs(root, targetSum)
        return self.numOfPaths
        
    
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
        ([10,5,-3,3,2,None,11,3,-2,None,1], 8, 3),
        ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22,3)
    ]
    for values,target, expected in test_cases:
        result = Solution().pathSum(build_tree(values),target)
        assert result == expected, f"For {values}, expected {expected}, got {result}"
        print(f"Input: {values}\nOutput: {result}")
        