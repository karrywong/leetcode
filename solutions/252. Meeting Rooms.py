class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort()
        temp = intervals[0]
        for interval in intervals[1:]:
            if temp[1] > interval[0]:
                return False
            else:
                temp = interval
        return True
