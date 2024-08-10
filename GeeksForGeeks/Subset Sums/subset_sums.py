class Solution:
    def combinations(self, arr, start, path, res):
        for i in range(start, len(arr)):
            path.append(arr[i])
            res.append(sum(path))
            self.combinations(arr, i+1, path, res)
            path.pop()

    def subsetSums(self, arr, n):
        res = [0]
        self.combinations(arr, 0, [], res)
        return res


if __name__ == '__main__':
    ob = Solution()
    ans = ob.subsetSums([2, 5, 8, 11, 13], 5)
    ans.sort()
    for x in ans:
        print(x, end=" ")
    print("")
