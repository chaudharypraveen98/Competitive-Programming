from typing import List


class Solution:
    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.backtrack(nums[0:i]+nums[i+1:], path+[nums[i]], res)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums, [], [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
