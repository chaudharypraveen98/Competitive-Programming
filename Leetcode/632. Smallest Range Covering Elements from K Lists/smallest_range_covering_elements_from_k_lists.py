from heapq import heappush, heappop
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        left = right = nums[0][0]
        for row in range(len(nums)):
            cur_val = nums[row][0]
            left = min(left, cur_val)
            right = max(right, cur_val)
            heappush(heap, (cur_val, row, 0))
        
        result = [left, right]
        while True:
            val, row, col = heappop(heap)
            col +=1
            if col == len(nums[row]):
                return result
            next_val = nums[row][col]
            heappush(heap, (next_val, row, col))
            right = max(right, next_val)
            left = heap[0][0]
            if right - left < result[1]-result[0]:
                result = [left, right]
            
sol = Solution()
print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))
print(sol.smallestRange([[1]]))