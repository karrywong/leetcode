class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # soln 0 - by tarun_____
        #Hint 1: For each column, find the number of consecutive ones ending at each position.
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: continue
                matrix[i][j] +=matrix[i-1][j]
        
        #Hint 2: For each row, sort the cumulative ones in non-increasing order and "fit" the largest submatrix.
        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            c = 1
            for val in row:
                if val == 0: break
                ans = max(ans, val*c)
                c += 1
        return ans
        
