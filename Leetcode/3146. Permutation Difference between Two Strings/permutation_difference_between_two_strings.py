from typing import List


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashmap = {}
        res = 0
        for i in range(len(s)):
            hashmap[s[i]] = i
        for j in range(len(t)):
            res += abs(hashmap[t[j]]-j)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPermutationDifference("abcde", "edbac"))
