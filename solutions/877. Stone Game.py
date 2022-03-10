class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #DP, same as problem 486. Predict the Winner
        #Time O(N^2), space O(N^2)
        dp = [[0]*len(piles) for _ in range(len(piles))]
        for i in range(len(piles)-1, -1, -1):
            for j in range(i, len(piles)):
                if i == j:
                    dp[i][j] = piles[i]
                else:
                    a = piles[i] - dp[i+1][j]
                    b = piles[j] - dp[i][j-1]
                    dp[i][j] = max(a,b)
        return dp[0][-1] >= 0 
