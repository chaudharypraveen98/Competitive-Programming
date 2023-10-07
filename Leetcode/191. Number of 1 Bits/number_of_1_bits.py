class Solution:
    # 1 Approach : Its simple just we need to find n & n-1 
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n>0:
            n = n & n-1
            ans+=1
        return ans
    # 2 Approach: Right and check bit 
    def hammingWeight1(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = ans + (n>>i&1)
        return ans


item  = Solution()
print(item.hammingWeight(678))
print(item.hammingWeight1(678))