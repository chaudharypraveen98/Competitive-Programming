# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        self.i = 0  # Pointer to track the current element in preorder
        
        def helper(upper_bound: int) -> TreeNode | None:
            # If we've processed all elements or the current element violates the BST property
            if self.i == len(preorder) or preorder[self.i] > upper_bound:
                return None
            
            # The current value belongs to this subtree
            val = preorder[self.i]
            self.i += 1
            
            root = TreeNode(val)
            # Left child can be anything up to the current node's value
            root.left = helper(val)
            # Right child can be anything up to the parent's upper bound
            root.right = helper(upper_bound)
            
            return root
            
        return helper(float('inf'))


def level_order(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    values = []
    queue = [root]
    index = 0
    while index < len(queue):
        node = queue[index]
        index += 1
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
    preorder = [8, 5, 1, 7, 10, 12]
    expected = [8, 5, 10, 1, 7, None, 12]
    root = Solution().bstFromPreorder(preorder)
    actual = level_order(root)

    print(f"Preorder: {preorder}")
    print(f"Level order: {actual}")
    print(f"Expected: {expected}")
    print(f"Pass: {actual == expected}")