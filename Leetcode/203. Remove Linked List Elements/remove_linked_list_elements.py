# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        curr, prev = head, None
        while curr:
            if curr.val == val:
                # it means we are at the starting , we get the val == head so we need to pop from head and curr

                # This is the special case handling , if head is same as val
                if curr == head:
                    head = head.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head


l = [3, 5, 6, 8]


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
print(displayLinkedList(item.removeElements(linked_list, 6)))
