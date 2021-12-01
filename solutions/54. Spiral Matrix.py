class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Second attempt, code cleaner, time O(N), space O(1) excluding the output array
        m, n = len(matrix), len(matrix[0])
        ans, size = [], m*n
        left, right = 0, n-1 #j
        up, down = 0, m-1 #i
        while len(ans) < size:
            for j in range(left, right+1):
                ans.append(matrix[up][j]) #left to right
            for i in range(up+1, down+1):
                ans.append(matrix[i][right]) #up to down
            if up != down:
                for j in range(right-1, left-1,-1):
                    ans.append(matrix[down][j])
            if left != right:
                for i in range(down-1, up, -1):
                    ans.append(matrix[i][left])
            left += 1
            up += 1
            right -= 1
            down -= 1
        return ans
        
        # #First attempt, direct solution, time O(N), space O(1) excluding the output array
        # m, n = len(matrix), len(matrix[0])
        # i, j = 0, 0
        # ans, size = [], m*n
        # left, right = -1, n
        # up, down = 0, m
        # while True:
        #     while j < right:
        #         ans.append(matrix[i][j])
        #         j += 1
        #     if len(ans) == m*n: break
        #     j -= 1
        #     right -= 1
        #     i += 1
        #     while i < down:
        #         ans.append(matrix[i][j])
        #         i += 1
        #     if len(ans) == m*n: break
        #     i -= 1
        #     down -= 1
        #     j -= 1
        #     while j > left: 
        #         ans.append(matrix[i][j])
        #         j -= 1
        #     if len(ans) == m*n: break
        #     j += 1
        #     left += 1
        #     i -= 1
        #     while i > up:
        #         ans.append(matrix[i][j])
        #         i -= 1
        #     if len(ans) == m*n: break
        #     i += 1
        #     up += 1
        #     j += 1
        # return ans
