class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        for i in range(len(sequence)):
            start = i
            wordIndex = 0
            substring_count = 0
            while start < len(sequence):
                if sequence[start] != word[wordIndex]:
                    break
                wordIndex += 1
                start += 1
                if wordIndex >= len(word):
                    wordIndex = 0
                    substring_count += 1
            res = max(substring_count, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxRepeating("ababc", "abab"))
