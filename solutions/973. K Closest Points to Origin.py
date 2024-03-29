class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Heap, Time O(Nlogk), Space O(k)
        return heapq.nsmallest(k, points, key=self.squared_distance)
        
#         # Sort the list with a custom comparator function, Time O(NlogN), Space O(N)
#         points.sort(key=self.squared_distance)
#         # Return the first k elements of the sorted list
#         return points[:k]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
