from collections import Counter
from heapq import heappop, heappush
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for item, count in counts.most_common():
            heappush(heap, (-count, item))
        remaining = k
        result = []
        while heap and remaining:
            _, item = heappop(heap)
            result.append(item)
            remaining -=1
        return result
    
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent( [1], 1))
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))