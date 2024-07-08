class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # (a0 + a1) % k = (a1 + a2) % k => a0 % k = a2 % k = a4 % k 
        # (a1 + a2) % k = (a2 + a3) % k => a1 % k = a3 % k 
        
        # nums = [1,2,3,4,5] -> [1,0,1,0,1] -> [1,0,1]
        # nums = [1,4,2,3,1,4] -> [1,1,2,0,1,1]
        
        dp = defaultdict(Counter)
        for a in nums:
            for b in range(k):
                dp[b][a % k] = max(dp[b][a % k], dp[a % k][b] + 1)
        return max(max(dp[a].values()) for a in range(k))
    
        # for a in [1,4,2,3,1,4]:
        #     for b in [0,1,2]:
        # dp = {0: {1:1}, 1: {1:2} ,2: {1:1} }          
        
