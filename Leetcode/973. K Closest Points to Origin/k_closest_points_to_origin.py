from heapq import heappush, heappop
from math import sqrt

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x,y in points:
            heappush(heap, (sqrt(x**2+y**2), x, y))
        result = []
        for _ in range(0, k):
            _, i,j = heappop(heap)
            result.append([i,j])
        return result
    
sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))