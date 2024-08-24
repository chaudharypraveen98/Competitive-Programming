class Solution:
    def get_path(self, row, col, k, arr, memo):
        if (row, col, k) in memo:
            print(memo)
            return memo[(row, col, k)]
        if row >= len(arr) or col >= len(arr):
            return 0

        k -= arr[row][col]
        if k == 0 and row == len(arr)-1 and col == len(arr)-1:
            return 1
        if k < 0:
            return 0
        bottom = self.get_path(row+1, col, k, arr, memo)
        right = self.get_path(row, col+1, k, arr, memo)
        result = right + bottom
        # we will store the element row, col with target and result , 1 means we have path else no
        memo[(row, col, k + arr[row][col])] = result
        return result

    def numberOfPath(self, n, k, arr):
        return self.get_path(0, 0, k, arr, {})


if __name__ == '__main__':
    ob = Solution()
    k = 20
    n = 5
    arr = [[2, 1, 4, 5, 4],
           [1, 3, 3, 3, 4],
           [3, 4, 2, 2, 3],
           [4, 5, 3, 3, 2],
           [3, 5, 5, 5, 1]]
    ans = ob.numberOfPath(n, k, arr)
    print(ans)
