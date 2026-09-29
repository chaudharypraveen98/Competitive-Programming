# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque([[root]])
        res = []
        while queue:
            nodes = queue.popleft()
            childs = []
            values = []
            for node in nodes:
                values.append(node.val)
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            if childs:
                queue.append(childs)
            if values:
                res.append(values)
        return res


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
    root_values = [3, 9, 20, None, None, 15, 7]
    root = build_tree(root_values)
    print(Solution().levelOrder(root))