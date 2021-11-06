class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #soln 0 - first attempt
        intervals.sort()
        ans = [intervals[0]]
        for interval in intervals[1:]:
            pre_interval = ans[-1]
            start, end = pre_interval[0], pre_interval[1]
            if interval[0] <= end:
                end = max(end, interval[1])
                start = min(start, interval[0])
                ans[-1] = [start, end]
            else:
                ans.append(interval)
        return ans
