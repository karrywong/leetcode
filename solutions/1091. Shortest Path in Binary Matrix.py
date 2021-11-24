class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #First attempt, BFS, Time O(N), Space O(N)
        #similar but easier than 752. Open the Lock
        n = len(grid)
        if grid[0][0]: return -1
        queue = collections.deque([(0,0,1)])
        seen = set()
        moves = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        ans = float('inf')
        while queue:
            r, c, count = queue.popleft()
            if r == n-1 and c == n-1: return count
            for r0, c0 in moves:
                x,y = r+r0, c+c0
                if 0<=x<n and 0<=y<n and grid[x][y] == 0:
                    if (x,y) not in seen:
                        seen.add((x,y))
                        queue.append((x,y,count+1))
        return -1
