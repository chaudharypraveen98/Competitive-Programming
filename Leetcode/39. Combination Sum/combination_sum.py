from typing import List


class Solution:
    def backtrack(self, arr, start, path, target, res):
        if target == 0:
            res.append(path[:])
            return
        if target < 0:
            return
        for i in range(len(arr)):
            if path and path[-1] > arr[i]:
                continue
            self.backtrack(arr, start+1, path+[arr[i]], target-arr[i], res)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_arr = sorted(candidates)
        return self.backtrack(sorted_arr, 0, [], target, [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([7, 3, 2], 18))
