from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            if node is None:
                return
            ans.append(node.val)
            for child in (node.children or []):
                dfs(child)
        dfs(root)
        return ans


if __name__ == "__main__":
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(Solution().preorder(root))