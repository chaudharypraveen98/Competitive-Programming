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
                    temp.append(res[i-1]+res[i])
            res = temp
        return self.create(cur+1, n, res)

    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        return self.create(1, rowIndex+1, res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(3))
