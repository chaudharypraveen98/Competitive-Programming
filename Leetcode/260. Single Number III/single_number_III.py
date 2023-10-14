class Solution:
    def singleNumber(self, nums):
        xored = 0
        for num in nums:
            xored ^= num
        mask = xored & -xored
        num1,num2=0,0
        for num in nums:
            if((num & mask)==0):
                num1 ^= num
            else:
                num2 ^= num
        return [num1,num2]

sol = Solution()
print(sol.singleNumber([1,2,1,3,2,5]))
