from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    parents = deque([root])
    index = 1

    while parents and index < len(values):
        parent = parents.popleft()

        if index < len(values) and values[index] is not None:
            parent.left = TreeNode(values[index])
            parents.append(parent.left)
        index += 1

        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            parents.append(parent.right)
        index += 1

    return root


def main() -> None:
    values = [5, 1, 4, None, None, 3, 6]
    root = build_tree(values)
    print(Solution().isValidBST(root))


if __name__ == "__main__":
    main()
