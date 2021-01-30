class Solution:
    def myPow(self, x: float, n: int) -> float:
        ### Soln 0 - recursion, fast
#         if n < 0: 
#             x, n = 1/x, -n
        
#         def recPower(x, n):
#             if n == 0: 
#                 return 1.0
#             half = recPower(x, n // 2)
#             if n % 2 == 0:
#                 return half* half
#             else:
#                 return half* half* x
#         return recPower(x,n)
    
        ### Soln 1 - another recusion by Haotian Li
        if x == 0:
            return 0
        elif n < 0:
            return self.myPow( 1/ x, -n)
        elif n == 0:
            return 1
        else:
            if n == 1:
                return x 
            else:
                remainderTwo = n % 2
                halfExponent = n // 2
                return (self.myPow(x,halfExponent) ** 2) * self.myPow(x,remainderTwo)
                
