class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # #Brute force, use sort, Time O(N^2), Space(N)
        # intervals.sort()
        # rooms = [intervals[0]]
        # for interval in intervals[1:]:
        #     for i in range(len(rooms)):
        #         if rooms[i][1] <= interval[0]:
        #             rooms[i] = interval
        #             break
        #     else:
        #         rooms.append(interval)
        # return len(rooms)
        
        # # Heap, time O(NlogN), space O(N)
        # intervals.sort()
        # free_rooms = [intervals[0][1]]
        # for interval in intervals[1:]:
        #     if free_rooms[0] <= interval[0]:
        #         heapq.heappop(free_rooms)
        #     heapq.heappush(free_rooms, interval[1])
        # return len(free_rooms)
        
        # Two pointers, time O(NlogN), space O(N)
        start_times = []
        end_times = []
        for s, e in intervals:
            start_times.append(s)
            end_times.append(e)
        start_times.sort()
        end_times.sort()
        
        s_ptr, e_ptr = 0, 0
        used_rooms = 0
        while s_ptr < len(start_times):
            if start_times[s_ptr] >= end_times[e_ptr]:
                used_rooms -= 1
                e_ptr += 1
            used_rooms += 1
            s_ptr += 1
        return used_rooms
