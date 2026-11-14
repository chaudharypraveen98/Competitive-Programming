from collections import deque
from heapq import heappop, heappush

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        self.total_moves = 0
        def dfs(node):
            if not node:
                return 0
            
            left_coins = dfs(node.left)
            right_coins = dfs(node.right)
            extra_coins = left_coins+right_coins+node.val-1
            self.total_moves += abs(extra_coins) # calculating extra coins
            return extra_coins
        
        dfs(root)
        return self.total_moves
    
    def distributeCoins1(self, root: TreeNode | None) -> int:
            self.total_moves = 0
            def dfs(node):
                if not node:
                    return (0,0)
                
                nodes_left,left_coins = dfs(node.left)
                nodes_right, right_coins = dfs(node.right)
                total_coins_req = left_coins+right_coins+node.val
                size = nodes_left+nodes_right+1 
                self.total_moves += abs(size-total_coins_req) # calculating extra coins
                return (size,total_coins_req)
            
            dfs(root)
            return self.total_moves
        
    
def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


if __name__ == "__main__":
    values = [0, 3, 0]
    root = build_tree(values)
    moves = Solution().distributeCoins(root)
    expected = 3

    print(f"Input: {values}")
    print(f"Moves: {moves}")
    print(f"Expected: {expected}")
    print(f"Pass: {moves == expected}")