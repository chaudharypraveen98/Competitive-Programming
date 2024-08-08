from typing import Optional
from collections import deque

from typing import List


class Solution:
    def combination(self, start, path, res):
        path.append(start.data)
        if start.left and start.right:
            self.combination(start.left, path, res)
            self.combination(start.right, path, res)
        elif start.left:
            self.combination(start.left, path, res)
        elif start.right:
            self.combination(start.right, path, res)
        else:
            res.append(path[:])
        path.pop()

    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        res = []
        self.combination(root, [], res)
        return res


######## Driver Code   ########

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
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
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def inputTree(treeString):
    root = buildTree(treeString)
    return root


def inorder(root):
    if (root == None):
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    treeString = "10 20 30 40 60"
    root = inputTree(treeString)

    obj = Solution()
    res = obj.Paths(root)

    IntMatrix().Print(res)
