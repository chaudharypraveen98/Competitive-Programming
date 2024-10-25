from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_water = 0
        while i < j:
            x = j-i
            min_height = min(height[i], height[j])
            max_water = max(max_water, min_height*x)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_water


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 3, 4, 5, 1, 1, 1]))
