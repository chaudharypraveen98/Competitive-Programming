# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        idx = {v: i for i, v in enumerate(postorder)}

        def dfs(pre_l: int, pre_h: int, post_l: int, post_h: int) -> TreeNode | None:
            if pre_l > pre_h:
                return None

            root_val = preorder[pre_l]
            node = TreeNode(root_val)

            if pre_l == pre_h:
                return node

            left_root_val = preorder[pre_l + 1]
            left_root_index = idx[left_root_val]
            left_size = left_root_index - post_l + 1

            node.left = dfs(pre_l + 1, pre_l + left_size, post_l, left_root_index)
            node.right = dfs(pre_l + left_size + 1, pre_h, post_l + left_size, post_h - 1)
            return node

        return dfs(0, len(preorder) - 1, 0, len(postorder) - 1)


def level_order(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    result: list[int] = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == "__main__":
    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]

    root = Solution().constructFromPrePost(preorder, postorder)
    output = level_order(root)
    print(output)

    assert output == [1, 2, 3, 4, 5, 6, 7]
    print("Test passed")