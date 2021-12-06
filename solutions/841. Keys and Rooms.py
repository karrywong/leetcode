class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #First attempt, DFS with hashmap
        #time O(N+E) where N is the number of rooms and E is the number of keys
        #space O(N) due to queue and seen
        seen = set([0])
        queue = collections.deque([rooms[0]])
        
        while queue:
            room = queue.popleft()
            for key in room:
                if key not in seen:
                    queue.append(rooms[key])
                    seen.add(key)
        
        return True if len(seen) == len(rooms) else False
