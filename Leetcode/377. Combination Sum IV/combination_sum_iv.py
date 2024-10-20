from typing import List


class Solution:
    def backtrack(self, arr, start, target, memo):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in memo:
            return memo[target]
        total = 0
        for i in range(len(arr)):
            total += self.backtrack(arr, start, target-arr[i], memo)
        memo[target] = total
        return total

    def combinationSum4(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.backtrack(candidates, 0, target, {})


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum4([1, 2, 3], 4))
