class Solution:
    def myPow(self, x: float, n: int) -> float:
        #cheating not allowed, return x**n
        if n == 0: return 1
        if -1 < x < 1: 
            x = 1/x
            n *= -1
        elif x == 1:
            return 1
        elif x == -1:
            return 1 if n%2==0 else -1
        # n != 0 and (x < -1 or x > 1)
        lib = {}
        nb = bin(abs(n))[2:][::-1] #n=3, bin(n) = "0b1010", nb = "0101"
        temp = x
        for i in range(1,len(nb)+1):
            lib[i] = temp
            temp *= temp
        
        ans = 1
        for i in range(len(nb)):
            if nb[i] == "1":
                ans *= lib[i+1]
        return ans if n > 0 else 1/ans
​
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
        # if x == 0:
        #     return 0
        # elif n < 0:
        #     return self.myPow( 1/ x, -n)
        # elif n == 0:
        #     return 1
        # else:
        #     if n == 1:
        #         return x 
        #     else:
        #         remainderTwo = n % 2
        #         halfExponent = n // 2
        #         return (self.myPow(x,halfExponent) ** 2) * self.myPow(x,remainderTwo)
