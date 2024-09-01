class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _helper(self, m, w, i, j, memo):
        if i < 0 or j < 0 or j >= len(m[0]) or i >= len(m) or ((i, j) in memo and memo[(i, j)]):
            return False
        if not w:
            return True
        if m[i][j] != w[0]:
            return 0
        memo[(i, j)] = True
        return any(self._helper(m, w[1:], i+p, j+q, memo) for p, q in self.directions)

    def find_in_all_dir(self, m, w):
        for i in range(len(m)):
            for j in range(len(m[0])):
                if self._helper(m, w, i, j, {}):
                    return 1
        return 0

    def isWordExist(self, board, word):
        return self.find_in_all_dir(board, word)


s = Solution()

m = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'],
     ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
w = "bcgkjn"
print("is word there in the matrix ", s.isWordExist(m, w))

m = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'],
     ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
w = "adeijp"
print("is word there in the matrix ", s.isWordExist(m, w))

m = array = [
    ['c', 'a', 'i'],
    ['e', 'd', 'd'],
    ['m', 'j', 'k'],
    ['e', 'v', 'x'],
    ['t', 'f', 's']
]

w = "je"
print("is word there in the matrix ", s.isWordExist(m, w))
