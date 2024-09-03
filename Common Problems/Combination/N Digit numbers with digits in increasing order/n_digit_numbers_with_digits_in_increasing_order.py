from typing import List


class Solution:
    def __init__(self):
        self.digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def backtrack(self, n, start, path, res):
        if len(path) >= n:
            res.append(int("".join(path[:])))
            return
        for i in range(start, 9):
            path.append(self.digits[i])
            self.backtrack(n, i+1, path, res)
            path.pop()

    def increasingNumbers(self, n: int) -> List[int]:
        res = [] if n > 1 else [0]
        self.backtrack(n, 0, [], res)
        return res

# Driver code


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    n = 8

    obj = Solution()
    res = obj.increasingNumbers(n)

    IntArray().Print(res)
