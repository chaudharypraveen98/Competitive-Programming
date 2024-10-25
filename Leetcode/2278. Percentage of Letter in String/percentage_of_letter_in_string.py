class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for ch in s:
            if ch == letter:
                count += 1
        return int(count/len(s)*100) if count else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.percentageLetter("sgawtb", "s"))
