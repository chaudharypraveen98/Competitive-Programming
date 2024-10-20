from typing import List


class Solution:
    def backtrack(self, arr, start, k, path, target, res):
        if target < 0 or len(path) > k or start > len(arr):
            return
        if target == 0 and len(path) == k:
            res.append(path[:])
            return

        for i in range(start, len(arr)):
            self.backtrack(arr, i+1, k, path+[arr[i]], target-arr[i], res)
        return res

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.backtrack([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, k, [], n, [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(1, 1))
