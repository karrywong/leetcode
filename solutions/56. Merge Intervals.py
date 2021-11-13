class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #soln 0 - first attempt with sorting, Time O(NlogN), Space O(N)
        intervals.sort()
        ans = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
                # ans[-1][0] = min(ans[-1][0], interval[0]) #Not necessary because of sorting
            else:
                ans.append(interval)
        return ans
