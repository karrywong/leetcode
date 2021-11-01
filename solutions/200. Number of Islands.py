class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #soln 1 - Leetcode Union Find, Time O(MxN), Space O(MxN)
        m, n = len(grid), len(grid[0])
        parent = {}
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    parent[i*n+j] = -1
                    self.count+=1
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    r,c = i,j
                    for (dr,dc) in [(0,-1),(0,1),(-1,0),(1,0)]:
                        newRow, newCol = r + dr, c + dc
                        if 0<=newRow<m and 0<=newCol<n and grid[newRow][newCol] == "1":
                            self.union(parent, r*n+c, newRow*n+newCol)
        return self.count 
    
    
    def find(self, parent, i):
        if parent[i] != -1:
            return self.find(parent, parent[i])
        else:
            return i
​
    def union(self, parent, a, b):
        rootA = self.find(parent,a)
        rootB = self.find(parent,b)
        if rootA != rootB:
            parent[rootA] = rootB
            self.count -= 1
            # print(a, b, parent, self.count)
        
        # #soln 0 - first attempt DFS, Time O(MxN), Space O(MxN)
        # m, n = len(grid), len(grid[0])
        # seen = set()
        # ans = 0
        # for r0, row in enumerate(grid):
        #     for c0, val in enumerate(row):
        #         if int(val) and (r0,c0) not in seen:
        #             stack = [(r0,c0)]
        #             seen.add((r0,c0))
        #             while stack:
        #                 r,c = stack.pop()
        #                 for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
        #                     if ((0 <= nr < m) and (0 <= nc < n) and int(grid[nr][nc]) and (nr, nc) not in seen):
        #                         stack.append((nr, nc))
