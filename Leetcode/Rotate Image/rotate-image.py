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
    
    def rotateByFourDiagonal(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        # you can use len(matrix[0]). we have used len(matrix) because its a nxn matrix
        left,right = 0, len(matrix)-1

        while left<right:
            # loop entire row except last element (left,right-1)
            for i in range(right-left):
                top,bottom = left,right

                # storing the top left value
                top_left = matrix[top][left+i]

                # swapping bottom left with top left
                matrix[top][left+i] = matrix[bottom-i][left]

                # swapping bottom right with bottom left
                matrix[bottom-i][left] =matrix[bottom][right-i]

                #swapping bottom right with top right
                matrix[bottom][right-i] = matrix[top+i][right]

                matrix[top+i][right]=top_left
            left+=1
            right-=1
        
    def rotateByTransposeAndReverse(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(1, len(matrix)):
            for col in range(row):
                matrix[row][col],matrix[col][row]= matrix[col][row],matrix[row][col]
        for row in range(len(matrix)):
            matrix[row]=matrix[row][::-1]
item  = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
item.rotateByTransposeAndReverse(matrix)
print(matrix)