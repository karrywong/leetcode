class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #soln 1 - ternary
        while n:
            n, r = divmod(n, 3)
            if r == 2: return False
        return True
        
        # #soln 0 - brute force exhaustion
        # #sum(3**0, 3**1, ..., 3**14) = 0.5*(3**15-1) = 7174453 < 10**7
        # pow3 = [3**i for i in range(14,-1,-1)]
        # ind = 0
        # while n > 0 and ind < 15:
        #     if n >= pow3[ind]:
        #         n -= pow3[ind]
        #     ind += 1
        # return True if n == 0 else False
            
        
