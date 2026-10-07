# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        items = []
        
        def dfs(node, i, j):
            if node is None:
                return
            items.append((j,i,node.val))
            if node.left:
                dfs(node.left, i+1, j-1)
            if node.right:
                dfs(node.right, i+1, j+1)
        dfs(root, 0,0)
        items.sort()
        
        current_index = 0
        res = []
        while current_index < len(items):
            level_items = []
            level_items.append(items[current_index][2])
            while current_index+1 < len(items) and items[current_index][0] == items[current_index+1][0]:
                current_index +=1
                level_items.append(items[current_index][2])
            res.append(level_items)
            current_index +=1
        return res


# ---------- Driver code ----------
def build_tree(values):
    """Build a binary tree from a level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def run_tests():
    sol = Solution()
    tests = [
        # (input list, expected output)
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        ([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        ([], []),
        ([1], [[1]]),
    ]
    for idx, (vals, expected) in enumerate(tests, 1):
        root = build_tree(vals)
        result = sol.verticalTraversal(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {idx}: {status}")
        print(f"  Input:    {vals}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")


if __name__ == "__main__":
    run_tests()