class Solution:
    def backtrack(self, arr, visited, path, res):
        if len(arr) == 0:
            key = "".join(map(str, path))
            if not key in visited:
                visited.add(key)
                res.append(path[:])
            return
        for i in range(0, len(arr)):
            path.append(arr[i])
            self.backtrack(arr[:i]+arr[i+1:], visited, path, res)
            path.pop()
        return res

    def uniquePerms(self, arr, n):
        arr.sort()
        return self.backtrack(arr, set(), [], [])


if __name__ == '__main__':
    n = 3
    arr = [1, 2, 1]

    ob = Solution()
    res = ob.uniquePerms(arr, n)
    for i in range(len(res)):
        for j in range(n):
            print(res[i][j], end=" ")
        print()
