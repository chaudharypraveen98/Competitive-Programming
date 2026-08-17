import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph ={ i:{} for i in range(n)}
        stops = [float('inf') for _ in range(n)]
        for item_src, item_dest, cost in flights:
            graph[item_src][item_dest] = cost
        heap = [(0,0, src)]
        while heap:
            c_cost, c_stop, c_src  = heapq.heappop(heap)
            if c_src==dst:
                return c_cost
            if c_stop > k or c_stop >= stops[c_src]:
                continue
            stops[c_src] = c_stop
            for neighbour, n_cost in graph[c_src].items():
                heapq.heappush(heap,(c_cost+n_cost,c_stop+1, neighbour))
        return -1

sol = Solution()
print(sol.findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))
print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3,1))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0 , 2, 1))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2,0))
print(sol.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1))