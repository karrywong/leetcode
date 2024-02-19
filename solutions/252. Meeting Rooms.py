class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Time O(NlogN), Space O(1)
        if not intervals: return True
        intervals.sort()
        end = intervals[0][1]
        for s, e in intervals[1:]:
            if end > s:
                return False
            end = e
        return True
