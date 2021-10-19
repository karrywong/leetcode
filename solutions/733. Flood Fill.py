class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:  
        #soln 1 - first attempt with recursion
        oldColor = image[sr][sc]
        if oldColor == newColor: return image
        m = len(image)
        n = len(image[0])
        
        def helper(i, j):
            if image[i][j] == oldColor:
                image[i][j] = newColor
                if i > 0: helper(i-1, j)
                if i < m-1: helper(i+1, j)
                if j > 0: helper(i, j-1)
                if j < n-1: helper(i, j+1)    
                    
        helper(sr, sc)
        return image
            
        
        
        
