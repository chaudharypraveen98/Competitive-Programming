### Approach
1. head.next must always contains the largest value
2. we get the largest value by recursively call.
3. compare the head and head.next
4. if head.next is greater than the head.val then head = head.next
5. other wise return head