from typing import List


class Solution:
    # O(n^2)
    def minOperations(self, boxes: str) -> List[int]:
        index_of_set = [idx for idx, i in enumerate(boxes) if i == "1"]
        res = []
        for idx in range(len(boxes)):
            temp = 0
            for j in index_of_set:
                temp += abs(j-idx)
            res.append(temp)
        return res

    # Optimized O(n)
    def minOperations1(self, boxes: str) -> List[int]:
        res = [0]*len(boxes)
        leftCount, leftCost, rightCount, rightCost = 0, 0, 0, 0
        for i in range(1, len(boxes)):
            if boxes[i-1] == "1":
                leftCount += 1
            leftCost += leftCount
            res[i] += leftCost
        for i in range(len(boxes)-2, -1, -1):
            if boxes[i+1] == "1":
                rightCount += 1
            rightCost += rightCount
            res[i] += rightCost
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations("001011"))
