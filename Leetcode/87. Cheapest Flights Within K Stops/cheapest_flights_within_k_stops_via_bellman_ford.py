from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf') for _ in range(n)]
        distances[src] = 0

        for _ in range(k+1):
            temp  = distances.copy() # Snapshot of previous round's results
            
            for u,v,w in flights:
                # Read from 'distances', update 'temp'
                if distances[u] != float('inf') and distances[u]+w < temp[v]:
                    temp[v] = distances[u]+w
            distances = temp # Advance to the new round

        return distances[dst] if distances[dst] != float('inf') else -1

sol = Solution()
print(sol.findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))
print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3,1))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0 , 2, 1))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2,0))
print(sol.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1))