from typing import List


class Solution:
    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path[:])
            return []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums[0:i]+nums[i+1:], path+[nums[i]], res)
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sorted_arr = sorted(nums)
        return self.backtrack(sorted_arr, [], [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1, 1, 3]))
