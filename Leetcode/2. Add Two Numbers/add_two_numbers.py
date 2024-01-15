class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
       # base conditon
        if l1 == None and l2 == None:
            return ListNode(1) if carry else None
        sum_digit = (l1.val if l1 else 0) + (l2.val if l2 else 0)+carry
        carry = sum_digit//10
        ans = ListNode(0)
        ans.val = sum_digit % 10
        ans.next = self.addTwoNumbers(
            l1.next if l1 else None, l2.next if l2 else None, carry)
        return ans


l1_vals = [9, 9, 9, 9, 9, 9, 9]
l2_vals = [9, 9, 9, 9]
# Create ListNode instances for l1 and l2


def create_list_node(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


l1 = create_list_node(l1_vals)
l2 = create_list_node(l2_vals)

item = Solution()
result = item.addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
