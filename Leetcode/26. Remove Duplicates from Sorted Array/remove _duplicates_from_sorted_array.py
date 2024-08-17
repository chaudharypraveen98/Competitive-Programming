from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i, j = 0, 1
    #     while i < len(nums):
    #         if nums[i] == nums[j]:
    #             nums.pop(j)
    #             continue
    #         i+=1
    #         j+=1
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i+1


sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
