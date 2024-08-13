class Solution:
    def __init__(self) -> None:
        self.mod = 10**9 + 7

    # This is similar to below approach but utilizes the fact only prev row is needed
    def create_triangle(self, row_no, n, prev_row):
        if row_no >= n:
            return prev_row
        temp_arr = []
        for i in range(row_no+1):
            if i == 0 or i == row_no:
                temp_arr.append(1)
            else:
                # prev_row[i-1]+prev_row[i] is the most fact of pascal triangle
                temp_arr.append((prev_row[i-1]+prev_row[i]) % self.mod)
        return self.create_triangle(row_no+1, n, temp_arr)

    def nthRowOfPascalTriangle(self, n):
        return self.create_triangle(0, n, [])

    # This method will form complete pascal triangle but will give ttl

    def create_triangle1(self, row_no, n, tr):
        if row_no >= n:
            return
        temp_arr = []
        for i in range(row_no+1):
            if i == 0 or i == row_no:
                temp_arr.append(1)
            else:
                temp_arr.append((tr[row_no-1][i-1]+tr[row_no-1][i]) % self.mod)
        tr.append(temp_arr)
        self.create_triangle(row_no+1, n, tr)

    def nthRowOfPascalTriangle1(self, n):
        triangle = []
        self.create_triangle(0, n, triangle)
        return triangle[n-1]


if __name__ == '__main__':
    ob = Solution()
    ans = ob.nthRowOfPascalTriangle(4)
    for x in ans:
        print(x, end=" ")
    print()
