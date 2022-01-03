class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #BFS, Time O(mn), Space O(mn)
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()
        space = set()
        bo = False
        for i,row in enumerate(rooms):
            for j, room in enumerate(row):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                if rooms[i][j] == 2147483647 and not bo:
                    bo = True
                    
        if not bo:
            return rooms
        
        dist = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                x,y = queue.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    r, c = x+dx, y+dy
                    if 0 <= r < m and 0 <= c < n:
                        if rooms[r][c] == -1 or 0:
                            continue
                        if dist < rooms[r][c]:
                            rooms[r][c] = dist
                            queue.append((r,c))
            dist += 1
