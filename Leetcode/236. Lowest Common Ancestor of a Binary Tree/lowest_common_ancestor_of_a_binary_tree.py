# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return node
            is_root_equal = node==p or node==q
            left = dfs(node.left)
            right = dfs(node.right)
            if is_root_equal:
                return node
            elif left is None or right is None:
                return left or right
            else:
                return node
        return dfs(root)
            
                
                    


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


if __name__ == "__main__":
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.left
    q = root.right
    ancestor = Solution().lowestCommonAncestor(root, p, q)
    print(ancestor.val if ancestor else None)

    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.left
    q = root.left.right.right
    ancestor = Solution().lowestCommonAncestor(root, p, q)
    print(ancestor.val if ancestor else None)