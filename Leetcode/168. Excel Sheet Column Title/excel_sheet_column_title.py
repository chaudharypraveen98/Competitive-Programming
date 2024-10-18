class Solution:
    def convertToTitle(self, columnNumber: int, res="") -> str:
        arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if (columnNumber > 26):
            q = columnNumber//26  # or we can use columnNumber-1 instead of q -= 1
            r = columnNumber % 26
            # handling remainder null case
            if r == 0:
                r = 26
                q -= 1
            return self.convertToTitle(q, res) + arr[r-1]
        return arr[columnNumber-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(52))
