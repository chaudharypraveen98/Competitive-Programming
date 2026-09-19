from heapq import heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)
        
        while len(heap) >1:
            y = -heappop(heap)
            x = -heappop(heap)
            if x==y:
                continue
            heappush(heap, -(y-x))
        return -heap[0] if heap else 0
        
    
sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))
print(sol.lastStoneWeight([1]))