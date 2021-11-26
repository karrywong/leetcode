class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #Old attempt - DP programming
        #Refer to almost identical problems, 5. Longest Palindromic Substring & 647. Palindromic Substrings
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                # if current left / right characters are equal, then extend the largest pal by 2
                # else, max between the two last largest palindromes found 
                dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j] else max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]
