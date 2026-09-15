from typing import List
from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        current_capital = w
        n = len(profits)
        
        items = [(capital[i], profits[i]) for i in range(n)]
        items.sort(key=lambda x: x[0])
        
        heap = []
        index = 0
        while True:
            if k==0:
                return current_capital
            while index < n:
                c, p = items[index]
                if current_capital >= c:
                    heappush(heap, -p)
                    index +=1
                else:
                    break
            if heap:
                current_capital += -heappop(heap)
                k -=1
            else:
                return current_capital
            
    
sol = Solution()
print(sol.findMaximizedCapital(2, 0,[1,2,3],[0,1,1]))
print(sol.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))
print(sol.findMaximizedCapital(1, 0, [1,2,3], [1,1,2]))