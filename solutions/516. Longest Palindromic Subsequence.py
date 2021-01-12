class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ### Soln from discussion by HT_Wang
        ### Similar questions: palindromic substrings, shortest palindrome
​
        n = len(s)
        dp = [[0]*(n) for _ in range(n) ]
        
        # handles cases for single character palindromes
        for i in range(n):
            dp[i][i] = 1
​
                    
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # if current left / right characters are equal, then extend the largest pal by 2
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                # else, max between the two last largest palindromes found 
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]
