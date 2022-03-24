class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        #My attempt with Union Find, time O(MxN), space O(MxN)
        grid = [[0]*n for _ in range(m)]
        self.count = 0
        self.root = collections.defaultdict(lambda: -1)
        ans = []
        moves = {(0,1), (1,0), (-1,0), (0,-1)}
        for x, y in positions:
            if not grid[x][y]: 
                self.count += 1
                grid[x][y] = 1
                self.root[x*n+y] = -1
                for dx, dy in moves:
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y]:
                        self.union(x*n+y, new_x*n+new_y)
                # print(x,y, self.root)
            ans.append(self.count)
        return ans
            
    def find(self, i):
        if self.root[i] != -1:
            return self.find(self.root[i])
        else:
            return i
​
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.root[rootA] = rootB
            self.count -= 1
                   
    #Stefan Pochmann's Union Find
        # counts, main, land = [], {}, {}
        # for i, j in positions:
        #     p = i, j
        #     main[p], land[p] = p, [p]
        #     for q in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
        #         if q in main:
        #             p, q = main[p], main[q]
        #             if p != q:
        #                 if len(land[p]) < len(land[q]):
        #                     p, q = q, p
        #                 land[p] += land[q]
        #                 for l in land.pop(q):
        #                     main[l] = p
        #     counts += len(land),
        #     # print(land, main)
        # return counts
