class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        #Similar but easier problem, 1024. Video Stitching
#         #DP soln by lee215, time O(NR), where R = ranges[i] <= 100, space O(N)
#         dp = [0] + [float('inf')] * n
#         for i, a in enumerate(ranges):
#             for j in range(max(i - a + 1, 0), min(i + a, n) + 1):
#                 dp[j] = min(dp[j], dp[max(0, i - a)] + 1)
#         return dp[n] if dp[n] < float('inf') else -1
​
        # Alternative
        max_reach = [0] * (n+1)
        for i, w in enumerate(ranges):
            l, r = max(i-w,0), min(i+w,n)
            max_reach[l] = max(max_reach[l], r)
        
        ans, l, r = 1, 0, max_reach[0]
        while r < n:
            new_r = max(max_reach[l:r+1])
            if r == new_r:
                return -1
            l, r = r+1, new_r
            ans += 1
        return ans 
            
#         # Leetcode suggested greedy, time O(N), space O(N)
#         max_reach = [0] * (n+1)
#         for i, w in enumerate(ranges):
#             l, r = max(i-w,0), min(i+w,n)
#             max_reach[l] = max(max_reach[l], r)
        
#         ans = 0
#         cur_end = 0 #current rightmost position 
#         next_end = 0 #next rightmost position 
#         for i in range(n+1):
#             if i > next_end: 
#                 return -1
#             if i > cur_end:
#                 ans += 1
#                 cur_end = next_end
#             next_end = max(next_end, max_reach[i])
            
#         return ans
