from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for idx, i in enumerate(words):
            if x in i:
                res.append(idx)
        return res

    def findWordsContaining1(self, words: List[str], x: str) -> List[int]:
        # list comprehension : faster
        return [idx for idx, word in enumerate(words) if x in word]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))
