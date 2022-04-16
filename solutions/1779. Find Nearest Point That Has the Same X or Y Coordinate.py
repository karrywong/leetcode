class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        #Cleaner soln by rock, time O(N), space O(1)
        index, smallest = -1, math.inf
        for i, (r, c) in enumerate(points):
            dx, dy = x - r, y - c
            if dx * dy == 0 and abs(dx + dy) < smallest:
                smallest = abs(dx + dy)
                index = i
        return index
    
        # #Time O(N), space O(N), straightforward
        # lookup = collections.defaultdict(list)
        # for i, point in enumerate(points):
        #     if point[0] == x or point[1] == y:
        #         dist = abs(point[0]-x) + abs(point[1]-y)
        #         lookup[dist].append(i)
        # if not lookup:
        #     return -1
        # minval = float('inf')
        # for key in lookup:
        #     minval = min(key, minval)
        # return lookup[minval][0]
