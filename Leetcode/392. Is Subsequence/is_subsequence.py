class Solution:
    def check(self, cur, s, t):
        if s == "":
            return True
        if cur == len(t):
            return False
        if s[0] == t[cur]:
            return self.check(cur+1, s[1:], t)
        return self.check(cur+1, s, t)

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.check(0, s, t)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("axc", "ahbgdc"))
