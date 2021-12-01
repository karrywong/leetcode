class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #First attempt, direct solution, time O(N), space O(N)
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        ans, size = [], m*n
        left, right = -1, n
        up, down = 0, m
        while True:
            while j < right:
                ans.append(matrix[i][j])
                j += 1
            if len(ans) == m*n: break
            j -= 1
            right -= 1
            i += 1
            while i < down:
                ans.append(matrix[i][j])
                i += 1
            if len(ans) == m*n: break
            i -= 1
            down -= 1
            j -= 1
            while j > left: 
                ans.append(matrix[i][j])
                j -= 1
            if len(ans) == m*n: break
            j += 1
            left += 1
            i -= 1
            while i > up:
                ans.append(matrix[i][j])
                i -= 1
            if len(ans) == m*n: break
            i += 1
            up += 1
            j += 1
        return ans
