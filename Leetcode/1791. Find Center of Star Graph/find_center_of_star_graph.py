class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u,v = edges[0]
        m,n = edges[1]
        if u==m or u==n:
            return u
        else:
            return v



sol = Solution()
print(sol.findCenter([[1,2],[5,1],[1,3],[1,4]]))
print(sol.findCenter([[1,2],[2,3],[4,2]]))