class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # #soln 2 - Leetcode DFS
        # seen = set()
        # def area(r,c):
        #     if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) \
        #             and (r,c) not in seen and grid[r][c]):
        #         return 0 
        #     seen.add((r,c))
        #     return 1+area(r-1,c)+area(r+1,c)+area(r,c-1)+area(r,c+1)
        # return max(area(r,c) for c in range(len(grid[0])) for r in range(len(grid)))
​
        # #soln 1 - Leetcode DFS iterative + stack
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
        
        #soln 0 - naive, greedy
#         m, n = len(grid), len(grid[0])
#         island = set() #keep track of island (i,j) visited
#         visited = {} #key: i-th island, values: (i,j)
#         area = {} #key: i-th island, values: area
#         ind = 0
        
#         def helper(i, j, ind):
#             if ind not in visited:
#                 if (i,j) not in island: island.add((i,j))
#                 visited[ind] = [(i,j)]
