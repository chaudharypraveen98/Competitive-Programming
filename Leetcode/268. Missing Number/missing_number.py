class Solution:
    def missingNumber(self, nums) -> int:
        sum_all = len(nums)*(len(nums)+1)//2
        zero_present = False
        for num in nums:
            if num==0:
                zero_present = True
            sum_all-=num
        return sum_all if zero_present else 0
    def missingNumber1(self, nums) -> int:
        xor=0
        for i in range(len(nums)):
            xor^=nums[i]
            xor^=i+1
        return xor

item  = Solution()
print(item.missingNumber1([9,6,4,2,3,5,7,0,1]))