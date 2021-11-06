class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # #soln 1 - first attempt, bit manipulation
        return not n&(n-1) and n&0x55555555 if n > 0 else False
    
        # #soln 0 - old attempt, recursion
        # if n < 1: return False
        # if n == 1: return True
        # else:
        #     if n%4: 
        #         return False
        #     else: 
        #         return self.isPowerOfFour(n/4)
        
​
