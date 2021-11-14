class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Completely failed attempts, LeetCode Greedy solution
        n = len(intervals)
        new_start, new_end = newInterval
        ans, idx = [], 0
        # add all intervals starting before newInterval
        while idx < n and intervals[idx][0] < new_start: 
            ans.append(intervals[idx])
            idx += 1
        
        if not ans or ans[-1][1] < new_start:     
            ans.append(newInterval) # if there is no overlap, just add the interval
        else:
            ans[-1][1] = max(ans[-1][1], new_end)  # if there is an overlap, merge with the last interval
            
        while idx < n:
            if ans[-1][1] < intervals[idx][0]: # if there is no overlap, just add an interval
                ans.append(intervals[idx])
            else: # if there is an overlap, merge with the last interva
                ans[-1][1] = max(ans[-1][1], intervals[idx][1])
            idx += 1
        return ans
