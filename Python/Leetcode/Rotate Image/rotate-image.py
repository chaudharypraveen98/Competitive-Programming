class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1,-1,-1):
            for j in range(n):
                matrix[j].append(matrix[i][j])
            matrix[i]=matrix[i][n:]

item  = Solution()
print(item.rotate([[1,2,3],[4,5,6],[7,8,9]]))