class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        #Optimized soln by tuang3142 using two pointers, time O(NlogN), space O(1)
        maxval = maxval_so_far = 0
        ends = sorted(events, key = lambda x : x[1])
        j = 0
        for s, e, val in sorted(events):
            while j < len(events) and ends[j][1] < s:
                maxval_so_far = max(maxval_so_far, ends[j][2])
                j += 1
            maxval = max(maxval, maxval_so_far+val)
        return maxval
            
        # #Heap soln by tuang3142, idea is to use heap to keep track of the end time and the maximum value so far
        # #Time O(NlogN), space O(N)
        # maxval = maxval_so_far = 0
        # hp = [] #(end, value)
        # heapq.heapify(hp)
        # for s, e, val in sorted(events):
        #     while hp and hp[0][0] < s:
        #         #if there is a pass event that end earlier than the current event, its value will be reflected in max_value_so_far
        #         maxval_so_far = max(maxval_so_far, hp[0][1])
        #         heapq.heappop(hp)
        #     maxval = max(maxval, maxval_so_far+val)
        #     heapq.heappush(hp, (e, val))
        # return maxval
        
#         #Failed attempt, wrong idea - should sort according to start/end times
#         tps = [(-val,s,e) for s,e,val in events]
#         heapq.heapify(tps)
#         tp1 = heapq.heappop(tps)
#         maxval = -tp1[0]
#         if tp1[1] > tps[0][2] or tps[0][1] > tp1[2]:
#             return maxval - tps[0][0]
#         else:
#             tp2 = heapq.heappop(tps)
​
#         while len(tps) > 0:
#             if tp1[1] > tps[0][2] or tps[0][1] > tp1[2]:
#                 return max(maxval, -1*(tp1[0]+tps[0][0]))
#             elif tp2[1] > tps[0][2] or tps[0][1] > tp2[2]:
#                 return max(maxval, -1*(tp2[0]+tps[0][0]))
#             else: #tp1 and tp2 always overlap
#                 tp1 = tp2
#                 tp2 = heapq.heappop(tps)
#         return maxval
