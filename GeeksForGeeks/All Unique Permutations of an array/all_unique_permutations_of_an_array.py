class Solution:
    def backtrack(self, arr, path, res):
        if len(arr) == 0:
            res.append(path[:])
            return
        for i in range(0, len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            self.backtrack(arr[:i]+arr[i+1:], path+[arr[i]], res)
        return res

    def uniquePerms(self, arr, n):
        arr.sort()
        return self.backtrack(arr, [], [])


if __name__ == '__main__':
    n = 3
    arr = [1, 2, 1]

    ob = Solution()
    res = ob.uniquePerms(arr, n)
    for i in range(len(res)):
        for j in range(n):
            print(res[i][j], end=" ")
        print()
