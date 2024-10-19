class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest = ""

        def expand_from_center(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        largest = s[0]

        for i in range(len(s)-1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)
            if len(odd) > len(largest):
                largest = odd
            if len(even) > len(largest):
                largest = even
        return largest
