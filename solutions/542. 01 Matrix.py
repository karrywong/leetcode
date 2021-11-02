class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # soln 1 - optimized BFS, Time O(MN), Space O(MN)
        m, n = len(mat), len(mat[0])
        queue = collections.deque()
        ans = [ [float('inf') for _ in range(n)] for _ in range(m) ]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i,j))
        
        while queue:
            r0, c0 = queue.popleft();
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                r, c = r0+dr, c0+dc
                if 0 <= r < m and 0 <= c < n:
                    if ans[r][c] > ans[r0][c0] + 1:
                        ans[r][c] = ans[r0][c0] + 1
                        queue.append((r,c))
        return ans
        
#         #soln 0 - failed attempt, stupid BFS
#         m, n = len(mat), len(mat[0])
#         ans = [ [0 for _ in range(n)] for _ in range(m) ]
        
#         for i in range(m):
