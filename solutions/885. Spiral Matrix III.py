class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        #Overthought problem, inspired by LeetCode's straightforward soln, time O(max(rows, cols)^2)
        r, c = rStart, cStart
        ans = [[r,c]]
        N = rows*cols
        if N == 1: return ans
        
        for cnt in range(1,2*N,2):
            for dr, dc, k in ((0,1,cnt), (1,0,cnt), (0,-1,cnt+1), (-1,0,cnt+1)): #right, down, left, up
                for _ in range(k):
                    r += dr
                    c += dc
                
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r,c])
                        if len(ans) == N:
                            return ans
