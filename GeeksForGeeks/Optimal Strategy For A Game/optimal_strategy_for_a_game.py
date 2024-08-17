class Solution:
    def __init__(self):
        self.memo = {}
        self.arr = []

    def helper(self, i, j):
        if i > j:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        # selecting from left - both player and opponent
        left = self.arr[i] + min(self.helper(i+1, j-1), self.helper(i+2, j))
        # selecting from end only
        right = self.arr[j] + min(self.helper(i+1, j-1), self.helper(i, j-2))
        self.memo[(i, j)] = max(left, right)
        return self.memo[(i, j)]

    def optimalStrategyOfGame(self, n, arr):
        self.memo = {}
        self.arr = arr
        return self.helper(0, n-1)

    # It will give TTL

    # def combinations(self, arr, turn, score):
    #     print(arr, turn, score)
    #     if len(arr) == 1:
    #         if turn:
    #             return score + arr[0]
    #         return score

    #     left = self.combinations(arr[1:], not turn, score)
    #     right = self.combinations(arr[:len(arr)-1], not turn, score)
    #     print(left, right)
    #     if turn:
    #         return max(left+arr[0], right+arr[-1])
    #     else:
    #         return min(left, right)


if __name__ == '__main__':
    n = 4
    arr = [8, 15, 3, 7]
    ob = Solution()
    print(ob.optimalStrategyOfGame(n, arr))
