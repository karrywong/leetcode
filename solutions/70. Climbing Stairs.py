class Solution:
    global memo
    memo = collections.defaultdict(int,{1:1, 2:2})
    def climbStairs(self, n: int) -> int:
        # #soln 1 - recursion w memoization
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if memo[n] > 0:
        #     return memo[n]
        # memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        # return memo[n]
        
        #soln 2 - Fibonacci formula
        sqrt5 = sqrt(5)
        m = n+1
        return int(0.5**m * ((1+sqrt5)**m - (1-sqrt5)**m) / sqrt5)
        
        # #soln 0 - dynamic programming
        # if n == 1:
        #     return 1 
        # if n == 2:
        #     return 2
        # lst = [1,2] + [0] * (n-2)
        # for i in range(2, n):
        #     lst[i] = lst[i-1]+lst[i-2]
        # return lst[-1]
