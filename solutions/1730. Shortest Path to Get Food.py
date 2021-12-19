class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        #Standard BFS - still failed, needed to read hints, similar to 542. 01 Matrix
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    queue = collections.deque([(i,j,0)])
                    seen = set((i,j))
                    break
            else:
                continue
            break
            
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            x, y, count = queue.popleft()
            if grid[x][y] == "#":
                return count
            for xm, ym in moves:
                x0, y0 = x+xm, y+ym
                if 0 <= x0 < m and 0 <= y0 < n and grid[x0][y0] != "X" and (x0,y0) not in seen:
                    queue.append((x0,y0,count+1))
                    seen.add((x0,y0))
        return -1
