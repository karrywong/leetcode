class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
      # loop over house 
      # loop over heater
        
      # house = 1, dist = Min([0, 3]) -> 0
      # house = 2, dist -> 1
      # house = 3, dist -> 1
    
      # house[i] , heater[j], heater[j+1]
    # house = 12, heater = [1,3,4,4,4,11]
    # (0,5) -> (3,5) -> (5,5) -> 4
    # house = 0, heater = [1,3,4,4,4,11]
    # (0,5) -> (0,2) -> (0,1) -> (0,0) -> -1
​
    # M = len(houses), N = len(heaters)
    # time O(NlogN + M*logN) = O(max(M,N)* logN), space O(1)
        def _get_heater_index(h):
            # h = 10, heaters = [1,3,4,11]
            # l,r = (0,2) -> (2,2) -> 2 -> 1
            # (0,3) -> (2,3) -> (3,3) -> 2
            l, r = 0, len(heaters)-1
            while l < r: # l=r
                mid = l + (r-l) // 2
                if (heaters[mid] == h):
                    return mid
                elif heaters[mid] > h:
                    r = mid
                else: 
                    l = mid + 1
            return l-1 if heaters[l] > h else l
    
        ans = 0
        heaters.sort()
        for h in houses:
            i = _get_heater_index(h)
            if i==len(heaters)-1:
                dist = h-heaters[i]
            elif i == -1:
                dist = heaters[i+1]-h
            else:
                dist = min(h-heaters[i],heaters[i+1]-h)
            ans = max(ans, dist)
            
        return ans
            
