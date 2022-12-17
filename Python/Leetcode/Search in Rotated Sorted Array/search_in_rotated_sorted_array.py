# 1 <= nums.length <= 5000

class Solution:     
        
    def search(self, nums, target) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = ((right+left)//2)
            is_1_sorted = nums[left]<=nums[mid]
            if target==nums[mid]:
                return mid
            elif is_1_sorted:
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1

item  = Solution()
# print(item.sorted_binary_search([0],7,0,1))
print(item.search([1],3))