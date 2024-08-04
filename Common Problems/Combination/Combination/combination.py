class Solution:

    def combinations(self, arr, start, path, res):
        for i in range(start, len(arr)):
            path.append(arr[i])
            res.append(path[:])
            self.combinations(arr, i+1, path, res)
            path.pop()

    def combinationSum(self, arr):
        res = []
        self.combinations(arr, 0, [], res)
        return res


ob = Solution()
result = ob.combinationSum([1, 2, 3, 4])
for row in result:
    print(*row)
if not result:
    print()
