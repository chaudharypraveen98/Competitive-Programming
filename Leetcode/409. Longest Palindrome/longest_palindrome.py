class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        unique_ch = set()
        for ch in s:
            if ch in unique_ch:
                ans += 2
                unique_ch.remove(ch)
            else:
                unique_ch.add(ch)
        return min(ans+1, len(s))


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("bb"))
