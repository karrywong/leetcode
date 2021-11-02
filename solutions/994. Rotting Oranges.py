class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #soln 0 - BFS
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh.add((i,j))
        if not queue: 
            if fresh:
                return -1
            else:
                return 0
        
        count = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                r0, c0 = queue.popleft();
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    r, c = r0+dr, c0+dc
                    if 0 <= r < m and 0 <= c < n:
                        if grid[r][c] == 0:
                            continue
                        if grid[r][c] < grid[r0][c0]:
                            grid[r][c] = 2
                            queue.append((r,c))
                            fresh.remove((r,c))
            count += 1
        
        return count if not fresh else -1
