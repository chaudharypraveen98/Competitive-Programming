import sys


class Solution:
    def __init__(self):
        self.newColor = 0
        self.prevColor = 0

    def helper(self, image, sr, sc):
        # handling the same current color and new Color
        if image[sr][sc] != self.newColor:
            image[sr][sc] = self.newColor
            # handling four directions
            if sr-1 >= 0 and image[sr-1][sc] == self.prevColor:
                self.helper(image, sr-1, sc)
            if sc-1 >= 0 and image[sr][sc-1] == self.prevColor:
                self.helper(image, sr, sc-1)
            if sc+1 < len(image[sr]) and image[sr][sc+1] == self.prevColor:
                self.helper(image, sr, sc+1)
            if sr+1 < len(image) and image[sr+1][sc] == self.prevColor:
                self.helper(image, sr+1, sc)

    def floodFill(self, image, sr, sc, newColor):
        self.newColor = newColor
        self.prevColor = image[sr][sc]
        self.helper(image, sr, sc)
        return image


sys.setrecursionlimit(10**7)

# Ans
# 2 2 2
# 2 2 0
# 2 0 1

n = 3
m = 3
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc, newColor = 1, 1, 2
obj = Solution()
ans = obj.floodFill(image, sr, sc, newColor)
for _ in ans:
    for __ in _:
        print(__, end=" ")
    print()
