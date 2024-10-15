from typing import List


class Solution:

    def calculate(self, cur, cost, memo):
        if cur >= len(cost):
            return 0

        if cur in memo:
            return memo[cur]

        optimized_cost = min(self.calculate(
            cur+1, cost, memo), self.calculate(cur+2, cost, memo)) + cost[cur]

        memo[cur] = optimized_cost
        return optimized_cost

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.calculate(0, cost, memo), self.calculate(1, cost, memo))


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
