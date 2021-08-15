class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while True:
                if data < current_node.data:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(data)
                        break
                elif data > current_node.data:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(data)
                        break
                else:
                    break


def height(head):
    if head is None:
        return -1
    left = height(head.left)
    right = height(head.right)
    return 1 + max(left, right)


if __name__ == '__main__':
    n = [2, 3, 4, 5, 10, 8, 6, 7]
    tree = BinaryTree()
    for i in n:
        tree.insert(i)

    print(height(tree.head)+1)
