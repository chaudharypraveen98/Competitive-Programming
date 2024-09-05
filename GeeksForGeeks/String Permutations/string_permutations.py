class Solution:
    def backtrack(self, s, path, res, repeat=1):
        if len(s) == 0:
            res.append("".join(path))
            return
        for i in range(0, len(s)):
            self.backtrack(s[:i]+s[i+1:], path+[s[i]], res, repeat)
        return res

    def permutation(self, s):
        sorted_arr = sorted(list(s))
        return sorted(self.backtrack(sorted_arr, [], []))


if __name__ == "__main__":
    s = "PRJJX"
    ob = Solution()
    ans = ob.permutation(s)
    for i in ans:
        print(i, end=" ")
    print()
