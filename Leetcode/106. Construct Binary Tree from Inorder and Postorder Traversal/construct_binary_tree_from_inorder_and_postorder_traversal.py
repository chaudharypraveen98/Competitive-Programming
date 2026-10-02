from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # Step 1: Map each value to its index in the inorder array for O(1) lookups
        inorder_indices = {value: index for index, value in enumerate(inorder)}
        
        # Step 2: Keep track of where we are currently in the preorder list
        postorder_index = len(inorder)-1
        
        
        def build(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            
            val = postorder[postorder_index]
            postorder_index -=1
            root = TreeNode(val)
            mid = inorder_indices[val]
            root.right = build( mid+1, right)
            root.left = build(left, mid-1)
            
            return root
        return build(0, len(inorder)-1)


def level_order(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while values and values[-1] is None:
        values.pop()
    return values


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = Solution().buildTree(preorder, inorder)
    print(level_order(root))