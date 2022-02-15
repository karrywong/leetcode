class NumMatrix:
    #Almost identical to problem 1314. Matrix Block Sum
    #prefixSum[i][j] = prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+mat[i][j]
    #ans[i][j] = prefixSum[i+k][j+k] - prefixSum[i-k-1][j+k] - prefixSum[i+k][j-k-1] + prefixSum[i-k-1][j-k-1]
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.prefixSum[i][j] = matrix[i][j]
                if i > 0:
                    self.prefixSum[i][j] += self.prefixSum[i-1][j]
                if j > 0:
                    self.prefixSum[i][j] += self.prefixSum[i][j-1]
                if i > 0 and j > 0:
                    self.prefixSum[i][j] -= self.prefixSum[i-1][j-1]
​
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefixSum[row2][col2]
        if row1 > 0 and col1 > 0:
            ans += self.prefixSum[row1-1][col1-1]
        if row1 > 0:
            ans -= self.prefixSum[row1-1][col2]
        if col1 > 0:
            ans -= self.prefixSum[row2][col1-1]
        return ans
            
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
