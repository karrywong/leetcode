class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # DFS, time O(MxN), space O(MxN)
        rows, cols = len(grid), len(grid[0])
        seen = set() #set of frozenset (immutable)
        dxy = ((0,1), (1,0), (0,-1), (-1,0))
​
        def _expand(stack:List[Tuple[int]]) -> List[Tuple[int]]:
            path = []
​
            while stack:
                r0, c0 = stack.pop()
                grid[r0][c0] = 0
                for dx, dy in dxy:
                    r1, c1 = r0+dx, c0+dy
                    if 0 <= r1 < rows and 0 <= c1 < cols and grid[r1][c1]:
                        stack.append((r1,c1))
                        path.append((r1-row, c1-col))
            return frozenset(path)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    start = [(row,col)]
                    path_frozen = _expand(start)
                    
                    if path_frozen not in seen:
                        seen.add(path_frozen)
        return len(seen)
