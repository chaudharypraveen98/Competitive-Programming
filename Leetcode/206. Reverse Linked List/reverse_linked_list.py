class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseList1(self, head):
        if head.next == None:
            return head

        def reverseListHelper(curr, prev):
            if curr:
                temp = curr.next
                curr.next = prev
                return reverseListHelper(temp, curr)
            else:
                return prev

        return reverseListHelper(head, None)


def create_list_node(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


l1 = create_list_node([1, 2, 3, 4, 5])

item = Solution()
result = item.reverseList1(l1)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
