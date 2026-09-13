from heapq import heappush, heappop
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        n = len(nums)
        for i in range(n):
            heappush(heap,(nums[i][0], i, 0))

        rowCount = [0]*n
        shortest = None
        start_index = 0
        items = []
        
        def is_range_formed():
            return all(rowCount)
        
        while heap:
            val, row,col = heappop(heap)
            rowCount[row] +=1
            items.append((row,val))
            if(is_range_formed()):
                
                while start_index < len(items):
                    start_row, _ = items[start_index]
                    if rowCount[start_row] > 1:
                        rowCount[start_row] -=1
                        start_index +=1
                    else:
                        break
                start_row, start_val = items[start_index]
                diff = val - start_val
                if (shortest is None or diff < shortest[0]):
                    shortest = (val - start_val, start_val, val)
                start_index +=1
                rowCount[start_row] -=1
            if col + 1 < len(nums[row]):
                heappush(heap,(nums[row][col+1], row,col+1))
        return [shortest[1], shortest[2]]
sol = Solution()
print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))
print(sol.smallestRange([[1]]))