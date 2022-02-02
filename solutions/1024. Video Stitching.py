class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # #DP soln 2, time O(NlogN), space O(N), exactly the same for a similar but harder problem:
        # # #1326. Minimum Number of Taps to Open to Water a Garden
        # dp = [0] + [float('inf')]* time
        # clips.sort()
        # for left, right in clips:
        #     if left <= time:
        #         for j in range(left, min(right, time)+1): #or also range(left+1, min(right, time)+1)
        #             dp[j] = min(dp[j], dp[left]+1)
        # return dp[time] if dp[time] < float('inf') else -1
    
        #DP soln, time O(NlogN), space O(N), exactly the same for a similar but harder problem:
        #1326. Minimum Number of Taps to Open to Water a Garden
        clips.sort()
        max_right_end = list(range(time+1))
        for left, right in clips:
            if left <= time:
                max_right_end[left] = min(right, time)
        count = 1
        l, r = 0, max_right_end[0]
        while True:
            if time <= r: return count
            new_r = max(max_right_end[l:r+1])
            if r == new_r: return -1
            l, r = r, new_r
            count += 1
            
