import sys
sys.setrecursionlimit(100000)


class Solution:
    ans = []

    def _helper(self, N):
        if N > 0:
            self.ans.append(N)
            self._helper(N-5)
        self.ans.append(N)

    def pattern(self, N):
        self.ans = []
        self._helper(N)
        return self.ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end=" ")
        print()
