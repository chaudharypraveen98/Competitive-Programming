from typing import List


class Solution:
    def __init__(self):
        self.phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

    def backtrack(self, digits, start, path, res):
        if start == len(digits):
            res.append("".join(path))
            return []
        all_chars = self.phone_map[digits[start]]
        for ch in all_chars:
            self.backtrack(digits, start+1, path+[ch], res)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        return self.backtrack(digits, 0, [], [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations(""))
