from typing import List
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap  = [nums[0]]
        for i in range(1,n):
            num = nums[i]
            if len(heap) < k:
                heappush(heap,num)
            elif num>heap[0]:
                heappop(heap)
                heappush(heap,num)
        return heap[-k]
                
sol = Solution()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))