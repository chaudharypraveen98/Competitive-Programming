class Solution:
    def findMaximumXOR(self, nums) -> int:
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefix = {num>>i for num in nums}
            ans += any(ans^1^a in prefix for a in prefix)
        return ans
    

sol = Solution()
print(sol.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))