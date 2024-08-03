class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Cleaner code, refer to 59. Spiral Matrix II
        count = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        ans = []
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0,0
        for _ in range(rows*cols):
            ans.append(matrix[row][col])
            visited.add((row,col))
            drow, dcol = directions[count]
            if row+drow in {-1, rows} or col+dcol in {-1, cols} or (row+drow,col+dcol) in visited:
                count = (count+1)%4
                drow, dcol = directions[count]
            row+=drow
            col+=dcol 
        return ans
​
        # #Second attempt, code cleaner, time O(N), space O(1) excluding the output array
        # m, n = len(matrix), len(matrix[0])
        # ans, size = [], m*n
        # left, right = 0, n-1 #j
        # up, down = 0, m-1 #i
        # while len(ans) < size:
        #     for j in range(left, right+1):
        #         ans.append(matrix[up][j]) #left to right
        #     for i in range(up+1, down+1):
        #         ans.append(matrix[i][right]) #up to down
        #     if up != down: #make sure that we're on a different row
        #         for j in range(right-1, left-1,-1):
        #             ans.append(matrix[down][j])
        #     if left != right: #make sure that we're on a different col
        #         for i in range(down-1, up, -1):
        #             ans.append(matrix[i][left])
        #     left += 1
        #     up += 1
        #     right -= 1
        #     down -= 1
        # return ans
