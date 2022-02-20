class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Totally stuck, Leetcode soln, Time O(MN), Space O(MN)
        #Remotely similar problems are 583. Delete Operation for Two Strings, 1143. Longest Common Subsequence
        #Also try 161. One Edit Distance
        word1, word2 = '#'+word1, '#'+word2
        m, n = len(word1), len(word2)
        dp = [[0] * n for _ in range(m)]
        for j in range(1,n):
            dp[0][j] = j
        for i in range(1,m):
            dp[i][0] = i
        for i in range(1,m):
            for j in range(1,n):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1)+1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
