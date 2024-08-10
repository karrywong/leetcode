class Solution:
    def __init__(self):
        self.bound = 10**9+7
    def countGoodNumbers(self, n: int) -> int:
        # (n=2) * (n=1) = 4*5
        # (n=3) = 5*4*5 = 5*(n=2)
        # (n=4) = 4*5*4*5=4**2 * 5**2 = (n=2)*(n=2)
        # (n=5) = 5*(n=4)=4**2 * 5**3 =5*(n=2)*(n=2)
        # (n=6) = 4**3 * 5**3
        # (n=7) = 4**3 * 5**4 = (n=4)*(n=2)*(n=1)
        # (n=8) = 4**4 * 5**4
        # (n=9) = 4**4 * 5**5 = 5*
        # (n=10) = 4**5 * 5**5 = (n=2)*(n=4)*(n=4)
        # n, ans = 4**i + 5**j, i+j =n, j==i or j==i+1
            
        def helper(x:int) -> int:
            if x==0:
                return 1
            if x==1:
                return 20
            
            fact = helper(x//2)
            if x%2==0:
                return fact*fact % self.bound
            else:
                return 20*fact*fact % self.bound
        
        return helper(n//2) * (5 if n%2==1 else 1) % self.bound
            
#         if n==1:
#             return 5
#         if n==2:
#             return 20
        
#         n_shift = n >> 1
#         fact = self.countGoodNumbers(n_shift)
#         if 
#             return (fact*fact) % self.bound
        
        
        # bound = 10**9+7
        # ans = 1
        # for i in range(1,n+1):
        #     factor = 5 if i%2==1 else 4
        #     ans *= factor
        #     ans %= bound
        # return ans
        
        # evens =  n//2
        # if n%2==1:
        #     odds = evens+1
        # else:
        #     odds = evens
        # bound = 10**9+7
        # ans = 4**evens % bound
        # ans *= 5**odds % bound
        # return ans % bound
