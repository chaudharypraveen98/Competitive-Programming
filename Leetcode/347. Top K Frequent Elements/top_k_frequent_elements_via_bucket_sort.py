from collections import Counter
from typing import List


class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    n = len(nums)

    # Buckets where index represents frequency (0 to n)
    buckets = [[] for _ in range(n + 1)]
    for item, count in counts.items():  # O(U) instead of O(U log U)
      buckets[count].append(item)

    results = []
    # Traverse backwards from highest possible frequency down to 1
    for freq in range(n, 0, -1):
      for item in buckets[freq]:
        results.append(item)
        if len(results) == k:
          return results

    return results
            
        
        
    
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent( [1], 1))
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))