class Solution:

    def buildTree(self, n, In, post):
        if not In or not post:
            return None
        root_val = post.pop()
        in_index = In.index(root_val)
        node = Node(root_val)
        node.right = self.buildTree(n, In[in_index+1:], post)
        node.left = self.buildTree(n, In[:in_index], post)
        return node


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# This funtcion is here just to test
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


if __name__ == '__main__':
    ob = Solution()
    preOrder(ob.buildTree(5, [9, 5, 2, 3, 4], [5, 9, 3, 4, 2]))
    print()
