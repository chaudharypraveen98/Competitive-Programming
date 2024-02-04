# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head):
        if not head:
            return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            head = head.next
        return head


l = [5, 2, 13, 3, 8]


def createLinkedList(l):
    if not l:
        return None
    head = ListNode(l[0])
    curr = head
    for i in l[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head


def displayLinkedList(l):
    curr = l
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next


linked_list = createLinkedList(l)
item = Solution()
print(displayLinkedList(item.removeNodes(linked_list)))
