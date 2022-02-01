"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
​
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        #Even simpler soln inspired by infinute, idea is to keep track of previous end point
        #Time O(NlogN), space O(N), where N is total number of intervals
        intervals = sorted([[event.start, event.end] for people in schedule for event in people])
        prev_end = intervals[0][1]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > prev_end:
                ans.append(Interval(prev_end, intervals[i][0]))
            prev_end = max(prev_end, intervals[i][1])
        return ans
        
#         #Simple soln inspired by thegreatnovice using two pointers, left and right
#         # iterate through intervals with left pointer
#         # if left.start > right.end, append the common free time to the ans
#         # else, assign right to the lastest-ended intervals we heve visited so far.
#         #Time O(NlogN), space O(N), where N is total number of intervals
        
#         intervals = sorted([[event.start, event.end] for people in schedule for event in people])
#         right = 1
#         left = 0
#         commonFree = []
#         while right < len(intervals):
#             if intervals[right][0] > intervals[left][1]:
#                 commonFree.append(Interval(intervals[left][1] ,intervals[right][0]))
#                 left = right
#             elif intervals[right][1] > intervals[left][1]: 
#                 left = right                
#             right += 1
#         return commonFree
