class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         #soln 2 - DP, time O(MN), space O(1)
#         m, n = len(mat), len(mat[0])
#         ans = [ [float('inf')] * n  for _ in range(m) ]
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] == 0: ans[i][j] = 0
#                 else:
#                     if i > 0: ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
#                     if j > 0: ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
​
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if ans[i][j] == 0: continue
#                 if i < m-1: ans[i][j] = min(ans[i][j], ans[i+1][j]+1)
#                 if j < n-1: ans[i][j] = min(ans[i][j], ans[i][j+1]+1)
#         return ans
        
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
        
#         #soln 0 - failed attempt, stupid BFS, Time O((MN)^2)
#         m, n = len(mat), len(mat[0])
#         ans = [ [0 for _ in range(n)] for _ in range(m) ]
        
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] == 0:
#                     continue          
#                 queue = collections.deque([(i,j)])
#                 count = 0
#                 bo = True
#                 while queue and bo:
#                     size = len(queue)
#                     for _ in range(size):
#                         r0, c0 = queue.popleft()
#                         if mat[r0][c0] == 0:
#                             ans[i][j] = count
#                             bo = False
#                             break
#                         for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
#                             r, c = r0 + dr, c0 + dc
#                             if 0 <= r < m and 0 <= c < n:
#                                 queue.append((r,c))
#                     count += 1
#         return ans            
