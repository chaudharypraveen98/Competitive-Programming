class Solution:
    def __init__(self) -> None:
        self.dfs_arr = set()

    def dfs(self, mat, i, j):
        if mat[i][j] == 'X':
            return
        self.dfs_arr[i][j] = True
        # above condition
        if i-1 >= 0 and self.dfs_arr[i-1][j] == False:
            self.dfs(mat, i-1, j)
        # left
        if j-1 >= 0 and self.dfs_arr[i][j-1] == False:
            self.dfs(mat, i, j-1)
        # right
        if j+1 < m and self.dfs_arr[i][j+1] == False:
            self.dfs(mat, i, j+1)
        # bottom
        if i+1 < n and self.dfs_arr[i+1][j] == False:
            self.dfs(mat, i+1, j)

    def helper(self, mat, n, m):
        # elements connected to boundary element must not be converted , rest can!
        for j in range(0, m):
            # top row
            if mat[0][j] == 'O':
                self.dfs(mat, 0, j)
            # bottom row
            if mat[n-1][j] == 'O':
                self.dfs(mat, n-1, j)
        for i in range(0, n):
            # left col
            if mat[i][0] == 'O':
                self.dfs(mat, i, 0)
            # right col
            if mat[i][m-1] == 'O':
                self.dfs(mat, i, m-1)

    def fill(self, n, m, mat):
        # you can maintain a set of visited node but arr is useful for debugging
        self.dfs_arr = [[False for _ in range(0, m)] for _ in range(0, n)]
        self.helper(mat, n, m)
        for i in range(0, n):
            for j in range(0, m):
                if mat[i][j] == 'O' and self.dfs_arr[i][j] == False:
                    mat[i][j] = "X"
        return mat


if __name__ == '__main__':
    n, m = 5, 4
    mat = [['X', 'X', 'X', 'X'],
           ['X', 'O', 'X', 'X'],
           ['X', 'O', 'O', 'X'],
           ['X', 'O', 'X', 'X'],
           ['X', 'X', 'O', 'O']]
    ob = Solution()
    ans = ob.fill(n, m, mat)
    for i in range(n):
        for j in range(m):
            print(ans[i][j], end=" ")
        print()
