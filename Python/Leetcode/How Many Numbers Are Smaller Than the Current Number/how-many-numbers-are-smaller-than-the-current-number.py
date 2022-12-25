class Solution:
    def smallerNumbersThanCurrent(self, nums):
        hash_set={}
        for i,val in enumerate(sorted(nums)):
            if val not in hash_set:
                hash_set[val]=i
        return [hash_set[j] for j in nums]
item  = Solution()
print(item.smallerNumbersThanCurrent([8,1,2,2,3]))