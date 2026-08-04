import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
            n = len(points)
            visited = [False]*n
            total_cost = 0
            min_distance = [float('inf') for i in range(n)]
            min_distance[0] = 0

            for _ in range(n):
                u = -1
                for j in range(n):
                    if not visited[j] and (u==-1 or min_distance[j]<min_distance[u]):
                        u = j
                total_cost += min_distance[u]
                visited[u] = True
                x1,y1 = points[u]
                for v in range(n):
                    if not visited[v]:
                        x2,y2 = points[v]
                        distance = abs(x1-x2)+abs(y1-y2)
                        if distance < min_distance[v]:
                            min_distance[v] = distance
            return total_cost
    def minCostConnectPoints1(self, points: List[List[int]]) -> int:
        n = len(points)
        adjacent_list = {v:{} for v in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(x1-x2)+abs(y1-y2)
                adjacent_list[i][j] = distance
                adjacent_list[j][i] = distance
        start = 0
        visited = {start}
        heap = []
        total_cost = 0
        def start_from_vertix(node):
            for neighbour, distance in adjacent_list[node].items():
                heapq.heappush(heap, (distance, neighbour))
        start_from_vertix(start)
        while heap:
            cost, v = heapq.heappop(heap)
            if v in visited:
                continue

            visited.add(v)
            total_cost += cost
            start_from_vertix(v)
        return total_cost



sol = Solution()
print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(sol.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))