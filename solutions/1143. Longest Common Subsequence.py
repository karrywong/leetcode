class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # #First attempts, followed hints 1 and 2, time O(MN), space O(MN)
        # m, n = len(text1), len(text2)
        # dp = [[0]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0: 
        #             dp[0][0] = 1 if text1[0] == text2[0] else 0
        #         elif j == 0:
        #             dp[i][0] = 1 if text1[i] == text2[0] else dp[i-1][0]
        #         elif i == 0: 
        #             dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j-1]
        #         else:
        #             dp[i][j] = dp[i-1][j-1]+1 if text1[i] == text2[j] else max(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]
        
        #Leetcode top-down recursion w memoization, time O(MN), space O(MN)
        def get_longest(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + get_longest(i+1,j+1)
            else:
                memo[(i,j)] = max(get_longest(i, j+1), get_longest(i+1, j))
            return memo[(i,j)]
        
        memo = {}
        return get_longest(0,0) 
