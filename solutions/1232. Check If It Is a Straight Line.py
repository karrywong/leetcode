class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        def slope(pt):
            val = pt[0]-x0
            return (pt[1]-y0) / val if val != 0 else float('inf') 
        return len(set(map(slope, coordinates[1:]))) == 1
