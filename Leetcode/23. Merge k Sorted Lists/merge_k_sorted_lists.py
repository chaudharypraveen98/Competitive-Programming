import heapq
from typing import List, Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # Unique tie-breaker ensures ListNode comparison is never attempted
        entry_id = 0
        for list in lists:
            if list:
                heapq.heappush(heap, (list.val, entry_id, list))
                entry_id +=1
        
        dummy_node = ListNode(0)
        curr = dummy_node
        
        while heap:
            _, _, item = heapq.heappop(heap)
            
            dummy_node.next = item
            dummy_node = dummy_node.next
            
            if item.next:
                heapq.heappush(heap, (item.next.val, entry_id, item.next))
                entry_id +=1
                
        return curr.next


# ==========================================
# DRIVER CODE & HELPERS
# ==========================================


def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Converts a standard Python list to a singly-linked list."""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a singly-linked list back into a Python list for easy verification."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    raw_input = [[1, 4, 5], [1, 3, 4], [2, 6]]

    # 1. Convert input matrices to array of ListNode heads
    lists = [build_linked_list(lst) for lst in raw_input]

    # 2. Run Solution
    sol = Solution()
    merged_head = sol.mergeKLists(lists)

    # 3. Format and print results
    output_list = linked_list_to_list(merged_head)
    print(f"Merged Result: {output_list}")
    assert output_list == [1, 1, 2, 3, 4, 4, 5, 6]
