# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        def find_path(node: TreeNode | None, target: int, path: list[str]) -> bool:
            if node is None:
                return False
            if node.val == target:
                return True

            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()

            return False

        start_path: list[str] = []
        dest_path: list[str] = []
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)

        # Find Lowest Common Ancestor (first index where paths diverge)
        i = 0
        limit = min(len(start_path), len(dest_path))
        while i < limit and start_path[i] == dest_path[i]:
            i += 1

        up_moves = "U" * (len(start_path) - i)
        down_moves = "".join(dest_path[i:])
        return up_moves + down_moves
            
                
    def getDirections_unoptimized(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        def dfs(node, edge=""):
            if node is None:
                return ("", False, False)

            start_found = node.val == startValue
            dest_found = node.val == destValue

            l_str, l_start, l_end = dfs(node.left, "L")
            r_str, r_start, r_end = dfs(node.right, "R")

            if l_start and l_end:
                return (l_str, True, True)
            if r_start and r_end:
                return (r_str, True, True)
            if l_start and r_end:
                return ("U" * len(l_str) + r_str, True, True)
            if r_start and l_end:
                return ("U" * len(r_str) + l_str, True, True)

            # Missing cases: current node is start or dest, and the other is in a subtree
            if start_found and (l_end or r_end):
                return (l_str if l_end else r_str, True, True)
            if dest_found and (l_start or r_start):
                down_from_child = l_str if l_start else r_str
                return ("U" * len(down_from_child), True, True)

            if l_start or l_end or r_start or r_end:
                return (
                    edge + (l_str or r_str),
                    start_found or l_start or r_start,
                    dest_found or l_end or r_end,
                )

            return (edge if (start_found or dest_found) else "", start_found, dest_found)

        return dfs(root)[0]
    

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
        ([5,1,2,3,None,6,4], 3,6,"UURL"),
        ([2,1], 2,1,'L'),
        ([1,None,10,12,13,4,6,None,15,None,None,5,11,None,2,14,7,None,8,None,None,None,9,3], 6,15, "UURR")
    ]

    for values, start, end, expected in test_cases:
        root = build_tree(values)
        result = Solution().getDirections(root, start, end)
        print(f"Tree: {values} -> path = {result} | expected = {expected}")