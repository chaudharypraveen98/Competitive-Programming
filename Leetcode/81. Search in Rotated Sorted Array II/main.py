class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def dnc(left, right):
            if left > right:
                return False
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid]==nums[right]:
                return dnc(left + 1, right-1)  

            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target <= nums[mid]:
                    return dnc(left, mid)
                return dnc(mid + 1, right)
            else:                        # Right half is sorted
                if nums[mid] <= target <= nums[right]:
                    return dnc(mid + 1, right) 
                return dnc(left, mid - 1)

        return dnc(0, len(nums) - 1)
sol = Solution()
print(sol.search([2,5,6,0,0,1,2], 3))