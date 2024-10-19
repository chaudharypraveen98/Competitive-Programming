class Solution:
    def get_longest(self, s, i, j, memo, longest):
        if i > j:
            return False
        if (i, j) in memo:
            return memo[(i, j)]
        if s[i] == s[j]:
            if j - i <= 1:
                memo[(i, j)] = True
                if len(s[i:j+1]) > len(longest[0]):
                    longest[0] = s[i:j+1]
                return True
            if self.get_longest(s, i+1, j-1, memo, longest):
                memo[(i, j)] = True
                if len(longest[0]) < len(s[i:j+1]):
                    longest[0] = s[i:j+1]
                return True

        memo[(i, j)] = False
        self.get_longest(s, i+1, j, memo, longest)
        self.get_longest(s, i, j-1, memo, longest)
        return memo[(i, j)]

    def longestPalindrome(self, s: str) -> str:
        longest = [""]
        memo = {}
        self.get_longest(s, 0, len(s)-1, memo, longest)
        return longest[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("aacabdkacaa"))
