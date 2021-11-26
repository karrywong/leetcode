class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp, count = [1]*n, [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]: #Think harder on how to use max(dp[i], dp[j]+1)
                    if dp[i] == dp[j]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j]+1:
                        count[i] += count[j]
        dp_max = max(dp)
        return sum(count[i] for i in range(n) if dp[i] == dp_max)
