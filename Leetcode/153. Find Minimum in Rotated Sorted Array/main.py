class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum MUST be in the unsorted right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the right half is sorted, meaning mid could be 
            # the minimum, or the minimum is to its left.
            else:
                right = mid
                
        return nums[left]

# Verification execution pass
sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))  # Output: 1