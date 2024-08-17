import heapq
​
​
class Solution:
    # time O(Nlogk), space O(k)
    # k is small or N ~ k, heap is useful
    # k ~ N/2, heap is similar as brute-force sorting O(NlogN)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [] #[dist,x,y]; max heaap
        heapq.heapify(hp)
        for point in points:            
            dist = -1*self.squared_distance(point)
            if len(hp) < k:
                heapq.heappush(hp,[dist,*point]) #O(logk)
            else:
                heapq.heappushpop(hp, [dist,*point]) #O(logk)
        return [[h[1], h[2]] for h in hp]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0]**2 + point[1]**2
​
