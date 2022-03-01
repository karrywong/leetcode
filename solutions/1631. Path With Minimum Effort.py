class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #LeetCode Modified Dijkstra's algorithm
        #time O(ElogV) = O(m*n*log(m*n)), space O(m*n) 
        m, n = len(heights), len(heights[0])
        diff_mat = [[float('inf')] * n for _ in range(m)]
        diff_mat[0][0] = 0
        visited = [[False] * n for _ in range(m)]
        hp = [(0,0,0)] #difference, x, y
        
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while hp:
            diff, x, y = heapq.heappop(hp)
            visited[x][y] = True
            
            for dx, dy in moves:
                x_new, y_new = x+dx, y+dy
                if 0<=x_new<m and 0<=y_new<n and not visited[x_new][y_new]:
                    cur_diff = abs(heights[x][y] - heights[x_new][y_new])
                    max_diff = max(cur_diff, diff_mat[x][y])
                    if diff_mat[x_new][y_new] > max_diff:
                        diff_mat[x_new][y_new] = max_diff
                        heapq.heappush(hp, (max_diff, x_new, y_new))
        return diff_mat[-1][-1]
