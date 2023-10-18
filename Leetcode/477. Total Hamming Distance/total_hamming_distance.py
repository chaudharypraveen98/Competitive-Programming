class Solution:
    def totalHammingDistance(self, nums) -> int:
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num>>i)&1
            # ones * zeros
            res += count * (len(nums)-count)
        return res
    
sol = Solution()
print(sol.totalHammingDistance([4,14,2]))

