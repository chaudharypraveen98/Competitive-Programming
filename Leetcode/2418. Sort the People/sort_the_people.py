from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapped = {}
        for i in range(len(names)):
            mapped[heights[i]] = names[i]
        res = []
        sorted_height = sorted(heights, reverse=True)
        for i in sorted_height:
            res.append(mapped[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
