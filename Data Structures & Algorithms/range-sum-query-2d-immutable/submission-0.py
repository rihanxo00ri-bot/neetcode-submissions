class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row =len(matrix)
        self.col= len(matrix[0])
        pre_sum=0

        self.pre_list  = [[0]*(self.col+1)  for _ in range(self.row+1)]

        for r in range(self.row):
            for c in range(self.col):
                  self.pre_list[r+1][c+1]= (matrix[r][c]+self.pre_list[r][c+1]+self.pre_list[r+1][c] -self.pre_list[r][c])
               
           
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.pre_list[row2+1][col2+1]
            -self.pre_list[row1][col2+1]
            -self.pre_list[row2+1][col1]
            +self.pre_list[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)