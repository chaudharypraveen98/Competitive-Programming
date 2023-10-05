
# Importing chain class from itertools
from itertools import chain

class Solution:
    def shuffle(self, nums, n):
        ans=[]
        for i in range(n):
            ans+=[nums[i],nums[n+i]]
        return ans
    def shuffle1(self, nums, n):
        return list[chain.from_iterable(zip(nums[:n], nums[n:]))]

item  = Solution()
print(item.shuffle([1,2,3,4,4,3,2,1],4))
print(item.shuffle1([1,2,3,4,4,3,2,1],4))