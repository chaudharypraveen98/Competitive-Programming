class Solution:
    def runningSum(self, nums):
        res =[]
        cummulative_sum=0
        for i in nums:
            cummulative_sum+=i
            res.append(cummulative_sum)
        return res


item  = Solution()
print(item.runningSum([1,2,3,4]))