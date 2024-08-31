from collections import deque


class Solution:
    # Complete the function below
    def _helper(self, queue, res=[]):
        if not queue:
            return res
        current_sum = 0
        next_que = []
        while queue:
            current_el = queue.pop(0)
            current_sum += current_el.data
            if current_el.right:
                queue.append(current_el.right)
            if current_el.left:
                next_que.append(current_el.left)
        res.append(current_sum)
        self._helper(next_que, res)
        return res

    def diagonalSum(self, root):
        return self._helper([root], [])


# Driver Code Starts
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    s = "10 8 2 3 5 2 N"
    root = buildTree(s)
    ob = Solution()
    res = ob.diagonalSum(root)
    for i in res:
        print(i, end=" ")
    print()
