class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #DP programming, almost identical to 1143. Longest Common Subsequence
        m, n = len(word1), len(word2)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: 
                    dp[0][0] = 1 if word1[0] == word2[0] else 0
                elif j == 0:
                    dp[i][0] = 1 if word1[i] == word2[0] else dp[i-1][0]
                elif i == 0: 
                    dp[0][j] = 1 if word1[0] == word2[j] else dp[0][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1]+1 if word1[i] == word2[j] else max(dp[i-1][j], dp[i][j-1])
        return (m-dp[-1][-1]) + (n-dp[-1][-1])
    
