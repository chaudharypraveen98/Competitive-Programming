class Solution:
    def get_alpha_numeric(self, s: str) -> str:
        arr = [ch.lower() for ch in s if ch.isalnum()]
        return ''.join(arr)

    def isPalindrome(self, s: str) -> bool:
        filter_str = self.get_alpha_numeric(s)
        return filter_str == filter_str[::-1]


if __name__ == '__main__':
    str = " "
    sol = Solution()
    print(sol.isPalindrome(str))
