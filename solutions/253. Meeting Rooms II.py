class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # #First attempt, use sort, Time O(N^2), Space(N)
        # if not intervals: 
        #     return 0
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
        
        #Priority Queue using Heap, Time O(NlogN), Space O(N)
        if not intervals: 
            return 0
        free_rooms = []
        intervals.sort()
        heapq.heappush(free_rooms, intervals[0][1])
        
        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)
