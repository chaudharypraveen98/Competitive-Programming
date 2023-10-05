class Solution:
    def differenceOfSum(self, nums) -> int:
        sum_cumm = 0
        for i in nums:
            sum_cumm +=i
            sum_cumm -= sum(int(j) for j in str(i))
        return sum_cumm

item  = Solution()
print(item.differenceOfSum([1,15,6,3]))