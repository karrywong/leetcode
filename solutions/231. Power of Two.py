class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        soln 3 - first attempt, bit manipulation
        return not n&(n-1) if n > 0 else False
        
        # #soln 2 - old attempt
        # if n < 0: return False
        # return True if bin(n)[2:].count("1") == 1 else False
​
        # #soln 1 - old attempt
        # while n % 2 == 0 and n > 1: n /= 2
        # return True if n == 1 else False
        
        # # soln 0 - old attempt
        # if n < 1: return False
        # if n == 1 or n == 2: return True
        # else: # n >= 3
        #     if n % 2: return False
        #     else: return self.isPowerOfTwo(n/2)
