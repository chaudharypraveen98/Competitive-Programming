import sys
sys.setrecursionlimit(100000)


class Solution:
    def sequence(self, n):
        mod = 10**9+7

        def _helper(N):
            if N == 1:
                return N, N
            prev, total = _helper(N-1)
            mul_temp = 1
            for i in range(prev+1, prev+1+N):
                mul_temp *= i
            return prev+N, total+mul_temp
        ans, total = _helper(n)
        return total % mod


if __name__ == '__main__':
    ob = Solution()
    ans = ob.sequence(998)
    print(ans)
