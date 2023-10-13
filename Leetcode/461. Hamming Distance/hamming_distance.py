class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        while x>0 or y>0:
            if((x&1) != (y&1)):
                count+=1
            x>>=1
            y>>=1
        return count
sol = Solution()
print(sol.hammingDistance(1,4))