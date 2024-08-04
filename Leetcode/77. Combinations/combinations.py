class Solution:
    def __init__(self):
        self.length = 0

    def combinations(self, arr, start, path, res):
        for i in range(start, len(arr)):
            path.append(arr[i])
            if len(path) == self.length:
                res.append(path[:])
            if len(path) < self.length:
                self.combinations(arr, i+1, path, res)
            path.pop()

    def combine(self, n: int, k: int):
        res = []
        self.length = k
        arr = [i for i in range(1, n+1)]
        self.combinations(arr, 0, [], res)
        return res
