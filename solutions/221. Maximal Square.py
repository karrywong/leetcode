class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #soln 1 - DP w Jake, Time O(MN), Space O(1)
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for j in range(n-1,-1,-1): #bottom row
            val = int(matrix[-1][j])
            matrix[-1][j] = val
            ans = max(ans, val)
        
        if m == 1: return ans
        
        for i in range(m-2,-1,-1): #last column
            val = int(matrix[i][-1])
            matrix[i][-1] = val
            ans = max(ans, val)
​
        if n == 1: return ans
        
        for i in range(m-2,-1,-1): #row
            for j in range(n-2,-1,-1): #col
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1])
                    ans = max(ans, matrix[i][j])
        
        return ans*ans
​
#         #soln 0 - Jake's idea
#         m = len(matrix)
#         n = len(matrix[0])
​
#         def checker(i,j):
#             # Finds the largest square with upper left corner at (i,j)
#             # assumes (i,j) entry is 1
#             width = 1
#             while i + width < m and j + width < n:
#                 if all(map(int,matrix[i+width][j:j+width])) and all(map(int,[matrix[x][j+width] for x in range(i,i+width+1)])):
#                     width += 1
#                 else:
#                     return width
#             return width
​
#         maxLen = 0
