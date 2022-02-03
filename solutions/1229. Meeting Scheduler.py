class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        #Alernative LeetCode soln using heap, tricky idea: if we find a common time slot, 
        #we know that the two-time slots couldn't possibly be for the same person 
        #since time slots for a single person do not overlap
        #Time O((M+N)log(M+N)), space O(M+N)
        
        #Very smart initialization, all intervals are longer than duration!
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)
        
        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0] # start1 <= start2
            if end1 >= start2 + duration:
                return [start2, start2+duration]
        return []            
        
        # #Inspired by LeetCode hint, use two pointers, time O(MlogM + NlogN), space O(1)
        # slots1.sort()
        # slots2.sort()
        # i, j = 0, 0
        # while i < len(slots1) and j < len(slots2):
        #     if slots1[i][0] < slots2[j][1] and slots1[i][1] > slots2[j][0]:
        #         #common slot
        #         start, end = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
        #         if end - start >= duration:
        #             return [start, start+duration]
        #     if slots1[i][1] <= slots2[j][1]:
        #         i += 1
        #     else:
        #         j += 1
        # return []
        
