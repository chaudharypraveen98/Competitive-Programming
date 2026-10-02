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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Step 1: Map each value to its index in the inorder array for O(1) lookups
        inorder_indices = {value: index for index, value in enumerate(inorder)}
        
        # Step 2: Keep track of where we are currently in the preorder list
        preorder_index = 0

        def build(left: int, right: int) -> TreeNode | None:
            nonlocal preorder_index
            
            # Base case: if there are no elements to construct the subtree
            if left > right:
                return None
            
            # Step 3: Pick the current root value from preorder and advance the pointer
            val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(val)
            
            # Step 4: Find where this value sits in the inorder array
            mid = inorder_indices[val]
            
            # Step 5: Recursively build left and right subtrees
            # Left subtree uses elements to the left of 'mid' in inorder
            root.left = build(left, mid - 1)
            # Right subtree uses elements to the right of 'mid' in inorder
            root.right = build(mid + 1, right)
            
            return root

        # We start by considering the entire inorder array from index 0 to len - 1
        return build(0, len(inorder) - 1)


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