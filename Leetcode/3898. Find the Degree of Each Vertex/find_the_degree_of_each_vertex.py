class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]
    
sol = Solution()
print(sol.findDegrees([[0,1,1],[1,0,1],[1,1,0]]))
print(sol.findDegrees([[0,1,0],[1,0,0],[0,0,0]]))