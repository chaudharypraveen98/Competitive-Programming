from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque([root])
        reverse = False
        res = []
        while queue:
            temp_res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                temp_res.reverse()
            res.append(temp_res)
            reverse = not reverse
        return res


if __name__ == "__main__":
    tests = [
        (
            TreeNode(3),
            [[3], [20, 9], [15, 7]],
        ),
        (
            TreeNode(1),
            [[1], [3, 2], [4, 5]],
        ),
    ]

    tests[0][0].left = TreeNode(9)
    tests[0][0].right = TreeNode(20)
    tests[0][0].right.left = TreeNode(15)
    tests[0][0].right.right = TreeNode(7)

    tests[1][0].left = TreeNode(2)
    tests[1][0].right = TreeNode(3)
    tests[1][0].left.left = TreeNode(4)
    tests[1][0].right.right = TreeNode(5)

    for idx, (root, expected) in enumerate(tests, start=1):
        result = Solution().zigzagLevelOrder(root)
        print(f"Test {idx}: {result}")
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"