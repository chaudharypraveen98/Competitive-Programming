from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allowed = set()
        for i in allowed:
            set_allowed.add(i)
        res = 0
        for word in words:
            is_allowed = True
            for ch in word:
                if ch not in set_allowed:
                    is_allowed = False
                    break
            if (is_allowed):
                res += 1
        return res

    def countConsistentStrings1(self, allowed: str, words: List[str]) -> int:
        set_allowed = set(allowed)
        # all short circuit if something false
        return sum(all(ch in set_allowed for ch in word) for word in words)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countConsistentStrings1(
        "ab", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
