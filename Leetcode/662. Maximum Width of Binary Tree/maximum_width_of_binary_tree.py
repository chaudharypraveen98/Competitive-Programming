# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        
        def bfs():
            res = 0
            queue = deque([])
            queue.append((root,0))
            while queue:
                level_size = len(queue)
                _, first_index = queue[0]
                _, second_index = queue[-1]
                res = max(res, second_index-first_index+1)

                for _ in range(level_size):
                    node, index = queue.popleft()
                    # it follows the heap structure, which take each node
                    if node.left:
                        queue.append((node.left, 2 * index))
                    if node.right:
                        queue.append((node.right, 2 * index + 1))
            return res

        return bfs()
    
def build_tree(values: list[int | None]) -> Optional[TreeNode]:
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
    test_cases = [
        ([1,3,2,5,None,None,9,6,None,7], 7),
        ([1,3,2,5,3,None,9], 4),
        ([1,3,2,5], 2),
    ]

    for values, expected in test_cases:
        root = build_tree(values)
        result = Solution().widthOfBinaryTree(root)
        print(f"Tree: {values} -> width = {result} | expected = {expected}")