class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #O(N^2), stupid idea
        #lookup = {1:0, 2:4, 3:2, 10:[1,3]} #key: day, values: position
        #arr = [0,0,0,0,0] of same length
        #loop over in [1,2,3,10]: #O(N) -> O(logN)
        
        #O(NlogN)
        # search space, sorted(BloomDay) #O(NlogN)
        # eg1, [1,2,3,10], [F,F,T,T]
​
        if len(bloomDay) < m*k:
            return -1
        days = sorted(set(bloomDay)) #python sorted, set->list
        l, r = 0, len(days)-1
        
        while l < r:
            mid = l + (r-l) // 2
            day = days[mid]
            arr = [1 if time <= day else 0 for i, time in enumerate(bloomDay)]
            
            count = 0
            for key, group in itertools.groupby(arr): #O(N)
                if key:
                    val = sum(group)
                    if val >= k:
                        count += val//k
            if count < m:
                l = mid+1
            else:
                r = mid
                
        return days[r]
