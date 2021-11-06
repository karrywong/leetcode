class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #soln 2 - Leetcode exhaustion
        #math.log10(2**31 - 1) / math.log10(3) ~ 19.6 and 3**19 = 1162261467
        if n < 1: return False
        return n > 0 and 1162261467 % n == 0;
        
        # # soln 1 - math
        # if n < 1: return False
        # x = math.log10(n) / math.log10(3)
        # return int(x) == x
    
        # soln 0 - old attempt, recursion
        # if n < 1:
        #     return False
        # if n == 1:
        #     return True
        # else:
        #     if n % 3 > 0:
        #         return False
        #     else:
        #         return self.isPowerOfThree(n/3)
