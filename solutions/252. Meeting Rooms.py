class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Time O(NlogN), Space O(1)
        if not intervals: return True
        intervals.sort()
        temp = intervals[0]
        for interval in intervals[1:]:
            if temp[1] > interval[0]:
                return False
            else:
                temp = interval
        return True
