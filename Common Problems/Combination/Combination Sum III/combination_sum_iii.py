class Solution:
    def __init__(self):
        self.length = 0
        self.target = 0

    def backtrack(self, arr, start, path, res):
        for i in range(start, len(arr)):
            if len(path) < self.length:
                path.append(arr[i])
                if sum(path) == self.target and len(path) == self.length:
                    res.append(path[:])
                if sum(path) < self.target:
                    self.backtrack(arr, i+1, path, res)
                path.pop()

    def combinationSum(self, K, target):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        self.length = K
        self.target = target
        self.backtrack(arr, 0, [], res)
        return res


ob = Solution()
result = ob.combinationSum(3, 9)
for row in result:
    print(*row)
if not result:
    print()
