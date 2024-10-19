class Solution:
    def recursion_with_memo(self, n, res, memo):
        if (n == 0):
            res += 1
            return res
        if n in memo:
            return memo[n]
        cal = self.recursion_with_memo(n-1, res, memo) + \
            (self.recursion_with_memo(n-2, res, memo) if n > 1 else 0)
        memo[n] = cal
        return cal

    def climbStairs(self, n: int) -> int:
        return self.recursion_with_memo(n, 0, {})


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(38))
