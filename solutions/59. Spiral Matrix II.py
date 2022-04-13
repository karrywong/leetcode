class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #LeetCode optimized, time O(N^2), space O(1)
        ans = [[None]*n for _ in range(n)]
        moves = [(0,1), (1,0), (0,-1), (-1,0)] #right, down, left, up
        r, c, d = 0, 0, 0
        for cnt in range(1, n*n+1):
            ans[r][c] = cnt
            nr, nc = r + moves[d][0], c + moves[d][1]
            if not 0 <= nr < n or not 0 <= nc < n or ans[nr][nc] is not None:
                d = (d+1) % 4
                nr, nc = r + moves[d][0], c + moves[d][1]
            r, c = nr, nc
        return ans
        
#         #First attempt, almost identical to 54. Spiral Matrix, time O(N^2), space O(1) excluding output array
#         ans = [[None]*n for _ in range(n)]
#         num, size = 1, n*n
#         left, right = 0, n-1 #i
#         up, down = 0, n-1 #j
        
#         while num <= n*n:
#             for j in range(left, right+1):
#                 ans[up][j] = num
#                 num += 1
#             for i in range(up+1, down+1):
#                 ans[i][right] = num
#                 num += 1
#             if up != down:
#                 for j in range(right-1, left-1,-1):
#                     ans[down][j] = num
#                     num += 1
#             if left != right:
#                 for i in range(down-1, up, -1):
#                     ans[i][left] = num
#                     num += 1
#             left += 1
#             right -= 1
#             up += 1
#             down -= 1
#         return ans
