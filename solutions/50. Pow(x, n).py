class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursion, time O(log(n)), space O(log(n))
        # if iterative, space -> O(1)
        if n < 0:
            x, n = 1/x, -n
        elif n == 0:
            return 1.0
        
        def helper(a, b) -> float:
            if b == 1:
                return a
            
            r = helper(a, b//2)
            r_sq = r * r
            return r_sq if b % 2 == 0 else a * r_sq
​
        return helper(x,n)
​
#         #cheating not allowed, return x**n
#         if n == 0: return 1
#         if -1 < x < 1: 
#             x = 1/x
#             n *= -1
#         elif x == 1:
#             return 1
#         elif x == -1:
#             return 1 if n%2==0 else -1
#         # n != 0 and (x < -1 or x > 1)
#         lib = {}
#         nb = bin(abs(n))[2:][::-1] #n=3, bin(n) = "0b1010", nb = "0101"
#         temp = x
#         for i in range(1,len(nb)+1):
#             lib[i] = temp
#             temp *= temp
        
#         ans = 1
#         for i in range(len(nb)):
#             if nb[i] == "1":
#                 ans *= lib[i+1]
#         return ans if n > 0 else 1/ans 
    
        ### Soln 1 - another recusion by Haotian Li
        # if x == 0:
