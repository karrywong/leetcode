class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #First attempt, Greedy approach to find max no. of disjoint intervals, time O(NlogN) due to sorting
        #min(#intervals removed st remaining are disjoint)
        #= len(intervals) - max(#intervals are disjoint)
        intervals.sort()
        count = 1 #max(#intervals are disjoint)
        end = intervals[0][1]
        for interval in intervals[1:]:
            if end <= interval[0]:
                count += 1
                end = interval[1]
            else:
                if end > interval[1]:
                    end = interval[1]
            
        return len(intervals) - count
​
    #[[0,4], [1,2], [2,3], [3,4]]
    #end = 4, count = 1
    #[1,2], end = 2, count =1
    #[2,3], end = 3, count = 2
