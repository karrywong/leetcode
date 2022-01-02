class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #Failed mock interview attempt, Leetcode recursion
        m, n = len(s), len(t)
        htb = [[None] * n  for _ in range(m)] #hashtable to speedup
        
        def helper(i, j):
            if j == n:
                return 1
            
            if i == m or m-i < n-j:
                return 0
            
            if htb[i][j] is not None:
                return htb[i][j]
            
            ans = helper(i+1,j) # Always make this recursive call
            if s[i] == t[j]: #only if there is a character match
                ans += helper(i+1,j+1)
            
            htb[i][j] = ans
            return ans        
​
        return helper(0,0)
