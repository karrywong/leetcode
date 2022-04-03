class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #Discussion
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
        
        # #My attempt, faster
        # x0, y0 = coordinates[0]
        # def slope(pt):
        #     val = pt[0]-x0
        #     return (pt[1]-y0) / val if val != 0 else float('inf') 
        # return len(set(map(slope, coordinates[1:]))) == 1
