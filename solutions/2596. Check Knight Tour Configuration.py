class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def is_valid(tp1: Tuple[int,int], tp2: Tuple[int,int]) -> bool:
            dxy = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
            for x,y in dxy:
                if tp1[0]+x == tp2[0] and tp1[1]+y == tp2[1]:
                    return True
            return False
            
        lookup = [(0,0) for _ in range(len(grid)*len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                lookup[grid[i][j]] = (i,j)
        
        if lookup[0] != (0,0): return False
        for i in range(len(lookup)-1):
            if not is_valid(lookup[i], lookup[i+1]):
                return False
        return True
        
