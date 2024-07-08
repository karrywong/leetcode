class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # [1,2,1,1,2,1,2] -> [1,0,1,1,0,1,0]
        
        dp = defaultdict(Counter)
        for a in nums: # a=2
            for b in range(2): #b=1, dp[1][0] = max subseq length ending in ...112 = dp[0][1]+1
                dp[b][a % 2] = max(dp[b][a % 2], dp[a % 2][b] + 1)
        return max(max(dp[a].values()) for a in range(2))
​
        # A = [a % 2 for a in nums]
        # print(A.count(0), A.count(1))
        # for k, g in groupby(A):
        #     print(k,*g)
        # print(len(list(groupby(A))))
        # return 0
