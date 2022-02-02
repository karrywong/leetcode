class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
#         #DP soln by lee215, time O(NR), where R = ranges[i] <= 100, space O(N)
#         dp = [0] + [float('inf')] * n
#         for i, a in enumerate(ranges):
#             for j in range(max(i - a + 1, 0), min(i + a, n) + 1):
#                 dp[j] = min(dp[j], dp[max(0, i - a)] + 1)
#         return dp[n] if dp[n] < float('inf') else -1
        
        #Soln by liketheflower, time O(N), space O(N)
        # For all location of taps, store the largest right reach point
        max_right_end = list(range(n+1))
        for i, a in enumerate(ranges):
            # left, right = max(0, i-a), min(n, i+a)
            # max_right_end[left] = max(max_right_end[left], right)
            max_right_end[max(0, i-a)] = min(n, i+a) #optimized since from left to right, 2nd time always wider coverage
        
        count, l, r = 1, 0, max_right_end[0]
        while True:
            if n <= r : return count
            new_r = max(max_right_end[l:r+1])
            if new_r == r: return -1
            l, r = r, new_r
            count += 1
        
        # #Failed attempt but feel close to the answer in terms of the logic...
        # intervals = []
        # for i, dist in enumerate(ranges):
        #     if dist > 0:
        #         intervals.append([i-dist, i+dist])
        # if not intervals:
        #     return -1
        # intervals.sort()
        # # print(intervals)
        # prev_end = intervals[0][1]
        # ind = 1
        # while ind < len(intervals) and intervals[ind][0] <= 0:
        #     prev_end = max(prev_end, intervals[ind][1])
        #     ind += 1
        # count = 1
        # # print(ind, prev_end)
        # for interval in intervals[ind:]:
        #     if n <= prev_end:
        #         break
        #     start, end = interval
        #     if start <= prev_end < end:
        #         count += 1
        #         prev_end = end
        # return count if n <= prev_end else -1
