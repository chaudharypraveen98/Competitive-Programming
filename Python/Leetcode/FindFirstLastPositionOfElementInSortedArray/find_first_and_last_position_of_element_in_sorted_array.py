class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums)-1
        while right>=left:
            mid = left +(right-left)//2
            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                leftest_index = rightest_index = mid
                while leftest_index >0 and nums[leftest_index]==nums[leftest_index-1]:
                    leftest_index -=1
                while rightest_index<len(nums)-1 and nums[rightest_index]==nums[rightest_index+1]:
                    rightest_index +=1
                return[leftest_index,rightest_index]
        return [-1,-1]
        

item  = Solution()
# Approach 1
print(item.searchRange([-1,-1,0,1,8],1))