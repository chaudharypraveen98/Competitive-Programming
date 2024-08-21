import sys
sys.setrecursionlimit(10**6)


class Solution:
    def graycode(self, n):
        if n == 1:
            return ['0', '1']
        ans1 = self.graycode(n-1)
        ans = []
        for sa in ans1:
            ans.append('0'+sa)
        # reversing
        for sa in ans1[::-1]:
            ans.append('1'+sa)
        return ans

    # Below is the most basic and simple program to learn/ understand how conversion works

    # def dfs(self, start, n, path, res):
    #     if start == n:
    #         res.append(self.convert_to_gray(path))
    #         return

    #     path += "0"
    #     self.dfs(start+1, n, path, res)
    #     path.pop()
    #     path += "1"
    #     self.dfs(start+1, n, path, res)
    #     path.pop()

    # def convert_to_gray(self, path):
    #     g_code = ""
    #     for j in range(len(path)):
    #         if j == 0:
    #             g_code += path[j]
    #         else:
    #             # if more like doing XOR, doing this to save type conversion to int
    #             g_code += ("0" if path[j-1] == path[j] else "1")
    #     return g_code

    # def graycode(self, n):
    #     res = []
    #     self.dfs(0, n, [], res)
    #     return res


if __name__ == "__main__":
    n = 15
    ob = Solution()
    l = ob.graycode(n)

    for x in l:
        print(x, end=" ")

    print()
