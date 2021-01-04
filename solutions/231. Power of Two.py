class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ### Soln 1
        # if n < 0: return False
        # return True if bin(n)[2:].count("1") == 1 else False
​
        ### Soln 2
        # while n % 2 == 0 and n > 1:
        #     n /= 2
        # return True if n == 1 else False
        
        ###Soln 3
        if n < 1: 
            return False
        if n in [1,2]: 
            return True
        else:
            if n % 2:
                return False
            else:
                return self.isPowerOfTwo( n/2 )
