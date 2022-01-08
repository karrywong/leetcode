class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #First attempt, time O(NlogN), Space O(1)
        points.sort(key = lambda x : x[1]) #keep track of minimal right end point
        count = 1
        target = points[0][1]
        for point in points[1:]:
            if point[0] > target: 
                target = point[1]
                count += 1
        return count
        
