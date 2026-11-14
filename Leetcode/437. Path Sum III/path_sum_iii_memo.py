# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        self.cache ={}
        # recursive to get result
        self.dfs(root, target, 0)
        
        # return result
        return self.result
    
    def dfs(self, root, target, curr_sum):
        if root is None:
            return
        
        curr_sum += root.val
        
        if curr_sum==target:
            self.result += 1
            
        # Current Section Sum = currPathSum - oldPathSum
        # we want that section sum to equal our target,  currPathSum - oldPathSum = target ( Section Sum )
        if(curr_sum-target) in self.cache:
            self.result += self.cache[curr_sum-target]
            
        if curr_sum in self.cache:
            self.cache[curr_sum] +=1
        else:
            self.cache[curr_sum] = 1
            
        self.dfs(root.left, target, curr_sum )
        self.dfs(root.right, target, curr_sum )
        
        self.cache[curr_sum] -=1
        
        
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
        