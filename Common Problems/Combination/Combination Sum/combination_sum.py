class Solution:
    def backtrack(self, start, arr, target, path, res):
        if not arr or target < 0 or start >= len(arr):
            return res
        if target == 0:
            res.append(path)
            return res
        for i in range(start, len(arr)):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            self.backtrack(i, arr, target-arr[i], path+[arr[i]], res)
        return res

    def combinationalSum(self, A, B):
        sorted_arr = sorted(A)
        return self.backtrack(0, sorted_arr, B, [], [])


if __name__ == '__main__':
    n = 5
    a = [8, 1, 8, 6, 8]
    s = 12
    ob = Solution()
    result = ob.combinationalSum(a, s)
    # (1 1 1 1 1 1 1 1 1 1 1 1)(1 1 1 1 1 1 6)(1 1 1 1 8)(6 6)
    for i in range(len(result)):
        print("(", end="")
        size = len(result[i])
        for j in range(size - 1):
            print(result[i][j], end=" ")
        if (size):
            print(result[i][size - 1], end=")")
        else:
            print(")", end="")
    print()
