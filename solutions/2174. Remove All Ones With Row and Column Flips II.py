class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        #Following hints, brute force, inspired by jayalen86's soln using backtracking
        #Time O(1), space O(1)
        m, n = len(grid), len(grid[0])
        ans, flips = float('inf'), 0
        rows, cols = set(), set()
        
        def backtrack():
            nonlocal flips, ans
            flag = False
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and i not in rows and j not in cols:
                        flag = True
                        rows.add(i)
                        cols.add(j)
                        flips += 1
                        backtrack()
                        rows.remove(i)
                        cols.remove(j)
                        flips -= 1
                        
            if not flag:
                ans = min(ans, flips)
        
        backtrack()
        return ans
