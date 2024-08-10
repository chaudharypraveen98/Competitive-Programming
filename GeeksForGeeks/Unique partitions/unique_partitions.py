class Solution:
    def combinations(self, N, path, res):
        if N == 0 and path:
            res.append(path[:])
            return
        for i in range(N, 0, -1):
            if path and path[-1] < i:
                continue
            path.append(i)
            self.combinations(N-i, path, res)
            path.pop()

    def UniquePartitions(self, n):
        res = []
        self.combinations(n, [], res)
        return res


if __name__ == '__main__':
    ob = Solution()
    ans = ob.UniquePartitions(4)
    for x in ans:
        print(x, end=" ")
    print("")
