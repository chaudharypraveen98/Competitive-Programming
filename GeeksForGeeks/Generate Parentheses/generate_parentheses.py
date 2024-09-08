class Solution:
    def backtrack(self, left, right, n, path, res):
        if left > n or right > n or right > left:
            return

        if left == n and right == n-1:
            res.append("".join(path[:])+")")
            return

        self.backtrack(left+1, right, n, path+["("], res)
        self.backtrack(left, right+1, n, path+[")"], res)
        return res

    def AllParenthesis(self, n):
        res = []
        self.backtrack(1, 0, n, ["("], res)
        return res


if __name__ == "__main__":
    n = 3
    ob = Solution()
    result = ob.AllParenthesis(n)
    result.sort()
    for i in range(0, len(result)):
        print(result[i])
