class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #First attempts, followed hints 1 and 2
        m, n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: 
                    dp[0][0] = 1 if text1[0] == text2[0] else 0
                elif j == 0:
                    dp[i][0] = 1 if text1[i] == text2[0] else dp[i-1][0]
                elif i == 0: 
                    dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1]+1 if text1[i] == text2[j] else max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
