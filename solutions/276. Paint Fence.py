class Solution:
    def numWays(self, n: int, k: int) -> int:
        #Failed to figure out the recurrence relation, ie
        #(I) different color than previous post, (k-1)*totalWays(i-1)
        #(II) same color as previous post, but (i-1)th post must be of different color as (i-2)th post
        # -> (k-1)*totalWays(i-2)
        
        #Soln 3: bottom-up DP
        if n == 1: 
            return k 
        if n == 2: 
            return k*k
        
        prev = k*k
        prevprev = k
        for i in range(3, n+1):
            curr = (k-1)*(prev + prevprev)
            prevprev = prev
            prev = curr
        return curr
        
        # # Soln 2: Recursion w memoization
        # memo = {1:k, 2:k*k} #base cases
        # def helper(i:int) -> int:
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = (k-1)*(helper(i-1)+helper(i-2))
        #     return memo[i]
        # return helper(n)
        
        # #Soln 1: Recursion + LRU cache
        # @lru_cache(maxsize=None)
        # def helper(i):
        #     if i == 1:
        #         return k
        #     if i == 2:
        #         return k*k
        #     return (k-1)*(helper(i-1)+helper(i-2))
        # return helper(n)
