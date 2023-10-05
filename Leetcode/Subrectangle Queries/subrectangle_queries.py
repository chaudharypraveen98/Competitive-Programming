class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = rectangle
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1,row2+1):
            for col in range(col1,col2+1):
                self.rectangle[row][col]=newValue
        

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
item  = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(item.getValue(0, 2))
item.updateSubrectangle(0, 0, 3, 2, 5);
print(item.getValue(0, 2))
print(item.getValue(3, 1))
item.updateSubrectangle(3, 0, 3, 2, 10);
print(item.getValue(3, 1))
print(item.getValue(0, 2))