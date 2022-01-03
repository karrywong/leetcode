class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        #Leetcode optimized BFS, clever, time O(M^2*N^2), space O(M*N)
        directions = {(1,0), (-1,0), (0,1), (0,-1)}
        m, n = len(grid), len(grid[0])
        dist = [[0]* n for _ in range(m)] #matrix to store total distance
        
        emptyLandValue = 0 
        minDist = float('inf')
        
        #BFS
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if grid[r][c] == 1:
                    minDist = float('inf')
                    queue.append((r,c))
                    
                    steps = 1
                    while queue:
                        size = len(queue)
                        
                        for _ in range(size):
                            x0, y0 = queue.popleft()
                            for dx, dy in directions:
                                x, y = x0+dx, y0+dy
                                
                                if 0 <= x < m and 0 <= y < n and grid[x][y] == emptyLandValue:
                                    grid[x][y] -= 1
                                    dist[x][y] += steps
                                    queue.append((x,y))
