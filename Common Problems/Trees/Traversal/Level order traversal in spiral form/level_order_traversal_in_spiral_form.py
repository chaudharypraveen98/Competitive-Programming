from collections import deque

# Iterative method


def findSpiral(root):
    if not root:
        return []
    q, is_left, res = [root], False, []

    while q:
        current_ans = []
        for node in q:
            current_ans.append(node.data)
        if is_left:
            res.extend(current_ans)
        else:
            res.extend(current_ans[::-1])

        next_nodes = []
        for node in q:
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        q, is_left = next_nodes, not is_left
    return res

# Recursive method


def bfs(que, left_dir, res):
    if not que:
        return
    curr_values = []
    for node in que:
        curr_values.append(node.data)
    if left_dir:
        res.extend(curr_values)
    else:
        res.extend(curr_values[::-1])

    next_nodes = []
    for node in que:
        if node.left:
            next_nodes.append(node.left)
        if node.right:
            next_nodes.append(node.right)
    bfs(next_nodes, not left_dir, res)


def findSpiral1(root):
    if not root:
        return []
    q, is_left, res = [root], False, []
    bfs(q, is_left, res)
    return res


###### Driver Code Below #####
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


# 10 20 60 40 30
if __name__ == "__main__":
    s = "10 20 30 40 60"
    root = buildTree(s)
    print("---USING ITERATIVE METHOD---")
    result = findSpiral(root)
    for value in result:
        print(value, end=" ")
    print()

    print("---USING RECURSIVE METHOD---")
    result = findSpiral1(root)
    for value in result:
        print(value, end=" ")
    print()
