class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for i in s:
            counter[i] = counter.get(i, 0) + 1
        for j in t:
            if j not in counter:
                return False
            else:
                counter[j] = counter[j] - 1
                if counter[j] == 0:
                    del counter[j]
        return not counter


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("cat", "tac"))
