class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ### Soln1 - Direct solution O(N)
        if not timeSeries: 
            return 0
        
        res = 0
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1] - timeSeries[i]
            if  diff >= duration:
                res += duration
            else:
                res += diff
                
        res += duration
        
        return res
