from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = list(map(int, data.split(",")))
        i = 0

        def build(low, high):
            nonlocal i
            if i == len(vals) or not (low < vals[i] < high):
                return None
            val = vals[i]
            i += 1
            node = TreeNode(val)
            node.left = build(low, val)
            node.right = build(val, high)
            return node

        return build(float('-inf'), float('inf'))


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    parents = deque([root])
    index = 1

    while parents and index < len(values):
        parent = parents.popleft()
        if values[index] is not None:
            parent.left = TreeNode(values[index])
            parents.append(parent.left)
        index += 1

        if index < len(values):
            if values[index] is not None:
                parent.right = TreeNode(values[index])
                parents.append(parent.right)
            index += 1

    return root


def level_order(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    values: list[int | None] = []
    nodes = deque([root])
    while nodes:
        node = nodes.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        nodes.append(node.left)
        nodes.append(node.right)

    while values and values[-1] is None:
        values.pop()
    return values


def main() -> None:
    root = build_tree([2, 1, 3])
    codec = Codec()
    encoded = codec.serialize(root)
    print("encoded", encoded)
    restored = codec.deserialize(encoded)
    print(level_order(restored))


if __name__ == "__main__":
    main()
