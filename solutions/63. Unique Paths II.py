class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:        
        ### Soln 0 - Dynamic programming
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 or n == 1:
            return 0 if sum(sum(obstacleGrid, [])) >= 1 else 1
        
        res = [[1 for _ in range(n)] for _ in range(m)]
        #If obstacle is in first row, behind are all zeros - very good observation by Jake
        valx = 1
        for idx, a in enumerate(obstacleGrid[0]): 
            if a == 1:
                valx = 0
            res[0][idx] = valx
            
        #If obstacle is in first column, below are all zeros - very good observation by Jake
        idy = 0
        valy = 1
        while idy < m: 
            if obstacleGrid[idy][0] == 1:
                valy = 0
            res[idy][0] = valy
            idy += 1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i-1][j] + res[i][j-1]
                else:
                    res[i][j] = 0
        print(res)
        return res[-1][-1]
        
