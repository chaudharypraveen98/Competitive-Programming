from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        n = len(equations)
        NOT_FOUND_VAL = -1.0
        for i in range(n):
            u,v = equations[i]
            w = values[i]
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = w
            graph[v][u] = 1/w
        ans = []
        def dfs(src,dst, visited=None):
            if src==dst:
                return 1.0
            if visited is None:
                visited = set()
            visited.add(src)
            for neigbhour, val in graph[src].items():
                if neigbhour in visited:
                    continue
                res = dfs(neigbhour, dst, visited)
                if res != NOT_FOUND_VAL:
                    return val*res
            visited.remove(src)
            return NOT_FOUND_VAL

            
        for u,v in queries:
            if u not in graph or v not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(u,v))
        return ans

sol = Solution()
print(sol.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(sol.calcEquation([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
print(sol.calcEquation([["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]]))