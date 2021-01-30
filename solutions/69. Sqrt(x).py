class Solution:
    def mySqrt(self, x: int) -> int:
        ### Newton's method, fastest
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
            
        return int(x1)
        
        ### built-in function
        # return floor(sqrt(x))
        
        ### Native Approach
        # if x <= 1: return x
        # if x == 2: return 1
        # for i in range(x):
        #     if i*i > x:
        #         return (i - 1)            
            
        
