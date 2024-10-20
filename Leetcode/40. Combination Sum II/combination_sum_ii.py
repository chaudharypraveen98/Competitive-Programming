from typing import List


class Solution:
    def backtrack(self, arr, start, path, target, res):
        if target == 0:
            res.append(path[:])
            return
        if target < 0 or start >= len(arr):
            return
        for i in range(start, len(arr)):
            # duplicates are removed at same level
            if i > start and arr[i] == arr[i-1]:
                continue
            self.backtrack(arr, i+1, path+[arr[i]], target-arr[i], res)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_arr = sorted(candidates)
        return self.backtrack(sorted_arr, 0, [], target, [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
