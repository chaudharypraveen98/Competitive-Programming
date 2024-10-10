from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for str in strs[1:]:
            smaller = longest if len(longest) < len(str) else str
            # handles ["ab", "a"] case if everything matches
            longest = longest[:len(smaller)]
            for i in range(len(smaller)):
                if str[i] == longest[i]:
                    continue
                else:
                    longest = str[:i]
                    break
        return longest


if __name__ == '__main__':
    arr = ["ab", "a"]
    sol = Solution()
    print(sol.longestCommonPrefix(arr))
