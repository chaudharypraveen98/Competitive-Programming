from typing import List


class Solution:
    def create(self, cur, n, res):
        if cur > n:
            return res
        else:
            temp = []
            for i in range(cur):
                if i == 0 or i == cur-1:
                    temp.append(1)
                else:
                    temp.append(res[-1][i-1]+res[-1][i])
            res.append(temp)
        return self.create(cur+1, n, res)

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        return self.create(1, numRows, res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(1))
