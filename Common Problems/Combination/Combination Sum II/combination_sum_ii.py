class Solution:
    def __init__(self):
        self.target = 0

    def combinations(self, arr, start, path, res):
        for i in range(start, len(arr)):
            # skip duplicate elements to avoid generating duplicate combinations
            if i > start and arr[i] == arr[i - 1]:
                continue
            path.append(arr[i])
            if sum(path) == self.target:
                res.append(path[:])
            # is array is sorted then its valid
            if sum(path) < self.target:
                self.combinations(arr, i+1, path, res)
            path.pop()

    def CombinationSum2(self, arr, n, k):
        res = []
        arr.sort()
        self.target = k
        self.combinations(arr, 0, [], res)
        return res


ob = Solution()
arr1 = [7, 14, 27, 22, 29, 11, 19, 9, 16, 14, 25, 25,
        23, 10, 12, 14, 6, 25, 6, 22, 17, 18, 4, 28, 24, 5, 3, 3, 11]
result = ob.CombinationSum2(arr1, 29, 30)
for row in result:
    print(*row)
if not result:
    print()
