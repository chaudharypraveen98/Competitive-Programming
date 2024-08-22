class Solution:
    def __init__(self):
        self.grid = []
        self.word = ""
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                           (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def search_work(self, row, col, wordIndex, direction):
        if (row < 0 or row >= len(self.grid) or
            col < 0 or col >= len(self.grid[0]) or
            wordIndex >= len(self.word) or
                self.grid[row][col] != self.word[wordIndex]):
            return False
        if wordIndex == len(self.word) - 1:
            return True
        dr, dc = direction
        return self.search_work(row + dr, col + dc, wordIndex + 1, direction)

    def search_starter(self, row, col, wordIndex):
        return any(self.search_work(row, col, wordIndex, direction) for direction in self.directions)

    def searchWord(self, grid, word):
        self.grid = grid
        self.word = word
        ans = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == word[0] and self.search_starter(row, col, 0):
                    ans.append([row, col])
        return ans

    # Below code is useful for understanding the intention behind it.

    # def __init__(self) -> None:
    #     self.grid = []
    #     self.word = ""

    # def search_work(self, row, col, wordIndex, dir):
    #     if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]) or wordIndex >= len(self.word) or self.grid[row][col] != self.word[wordIndex]:
    #         return False

    #     if wordIndex == len(self.word)-1:
    #         return True
    #     if dir == "left":
    #         if self.search_work(row, col-1, wordIndex+1, "left"):
    #             return True
    #     if dir == "right":
    #         if self.search_work(row, col+1, wordIndex+1, "right"):
    #             return True
    #     if dir == "up":
    #         if self.search_work(row-1, col, wordIndex+1, "up"):
    #             return True
    #     if dir == "bottom":
    #         if self.search_work(row+1, col, wordIndex+1, "bottom"):
    #             return True
    #     if dir == "upleft":
    #         if self.search_work(row-1, col - 1, wordIndex+1, "upleft"):
    #             return True
    #     if dir == "upright":
    #         if self.search_work(row-1, col+1, wordIndex+1, "upright"):
    #             return True
    #     if dir == "bottomleft":
    #         if self.search_work(row+1, col-1, wordIndex+1, "bottomleft"):
    #             return True
    #     if dir == "bottomright":
    #         if self.search_work(row+1, col+1, wordIndex+1, "bottomright"):
    #             return True
    #     return False

    # def search_starter(self, row, col, wordIndex):
    #     arguments = ["left", "right", "up", "bottom",
    #                  "upleft", "upright", "bottomleft", "bottomright"]
    #     if any(self.search_work(row, col, wordIndex, arg) for arg in arguments):
    #         return True
    #     return False

    # def searchWord(self, grid, word):
    #     self.grid = grid
    #     self.word = word
    #     ans = []
    #     for row in range(len(grid)):
    #         for col in range(len(grid[0])):
    #             if grid[row][col] == word[0] and self.search_starter(row, col, 0):
    #                 ans.append([row, col])
    #     return ans


if __name__ == '__main__':
    grid = [
        ["d", "d", "e", "b", "a", "c", "d", "b", "d", "c", "e", "c", "b"],
        ["c", "c", "c", "c", "c", "c", "a", "e", "c", "b", "e", "a", "b"],
        ["b", "e", "e", "e", "d", "b", "c", "d", "c", "a", "d", "b", "c"],
        ["d", "a", "c", "a", "a", "a", "e", "a", "e", "b", "d", "c", "d"]
    ]
    word = "dd"
    obj = Solution()
    ans = obj.searchWord(grid, word)
    for _ in ans:
        for __ in _:
            print(__, end=" ")
        print()
    if len(ans) == 0:
        print(-1)
    # Expected Output:
    # 0 0
    # 0 1
    # 2 10
    # 3 10
