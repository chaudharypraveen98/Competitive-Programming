# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        def dfs(node):
            if node is None:
                return 
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans


if __name__ == "__main__":
    root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    print(Solution().preorderTraversal(root))