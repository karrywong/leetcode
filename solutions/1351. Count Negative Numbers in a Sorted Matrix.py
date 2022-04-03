class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #soln 2 - time O(M+N), space O(1), by rock
        r, c, cnt = m - 1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        return cnt
        
        # #soln 1 - brute force, time O(M*N), space O(1)
        # if (m, n) == (1, 1): return int(grid[0][0] < 0)
        # i, j = 0, 0
        # while j < n-1 and grid[i][j+1] >= 0:
        #     j += 1
        # while i < m-1 and grid[i+1][j] >= 0:
        #     i += 1
        # ans = (i+1)*(n-j-1)
        # for k in range(i+1, m):
        #     while j >= 0 and grid[k][j] < 0:
        #         j -= 1
        #     if j == -1: 
        #         ans += (m-k)*n
        #         break
        #     ans += (n-j-1)
        # return ans
