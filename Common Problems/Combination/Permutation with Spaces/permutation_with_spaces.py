class Solution:
    def backtrack(self, s, start, path, res):
        if start >= len(s):
            res.append(" ".join(path))
            return
        for str_len in range(1, len(s[start:])+1):
            path.append(s[start:start+str_len])
            self.backtrack(s, start+str_len, path, res)
            path.pop()
        return res

    def permutation(self, s):
        return self.backtrack(s, 0, [], [])


if __name__ == '__main__':
    ob = Solution()
    S = "A"
    ans = ob.permutation(S)
    write = ""
    for i in ans:
        write += "(" + i + ")"
    print(write)
