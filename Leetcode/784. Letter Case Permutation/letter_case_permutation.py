from typing import List


class Solution:
    def recursive(self, s, cur, path, res):
        if cur == len(s):
            res.append(path)
            return
        ascii_val = ord(s[cur])
        self.recursive(s, cur+1, path+s[cur], res)
        if ascii_val >= 97 and ascii_val <= 122:
            self.recursive(s, cur+1, path+s[cur].upper(), res)
        elif ascii_val >= 65 and ascii_val <= 90:
            self.recursive(s, cur+1, path+s[cur].lower(), res)
        return res

    def letterCasePermutation(self, s: str) -> List[str]:
        return self.recursive(s, 0, "", [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCasePermutation("a1b2"))
