class Solution:
    def check_palindrome(self, s):
        if s == "" or len(s) == 1:
            return True
        if s[0] == s[-1]:
            return self.check_palindrome(s[1:-1])
        return False

    def _helper(self, s, start, path, res):
        if start > len(s):
            if (s == ""):
                res.append(path[:])
            return
        if self.check_palindrome(s[:start]):
            path.append(s[:start])
            self._helper(s[start:], 1, path, res)
            path.pop()
        self._helper(s, start+1, path, res)

    def allPalindromicPerms(self, S):
        res = []
        self._helper(S, 1, [], res)
        return res


if __name__ == '__main__':

    S = "g"

    ob = Solution()
    allPart = ob.allPalindromicPerms(S)
    for i in range(len(allPart)):
        for j in range(len(allPart[i])):
            print(allPart[i][j], end=" ")
        print()
