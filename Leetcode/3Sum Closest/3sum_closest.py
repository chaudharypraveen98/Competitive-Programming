class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff = None
        closest_sum= None
        print(nums)
        for i in range(len(nums)-2):
          left = i+1
          right = len(nums)-1
          while left<right:
            sum_three = nums[i]+nums[left]+nums[right]
            new_diff = abs(target-sum_three)
            if diff is None or (diff and new_diff <diff):
              diff = new_diff
              closest_sum=sum_three
            if sum_three>target:
              right-=1
            elif sum_three<target:
              left+=1
            else:
              return target
        return closest_sum
            
item  = Solution()
print(item.threeSumClosest([0,0,0],1))