class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #maximum from right in values[j]-j
        maxright = [0]*(len(values)-1)
        maxright[-1] = values[-1]-len(values)+1
        for i in range(len(values)-2, 0, -1):
            maxright[i-1] = max(maxright[i], values[i]-i)
        
        #maximize values[i]+i+values[j]-j, j > i
        ans = float('-inf') 
        for i, val in enumerate(values[:-1]):
            ans = max(ans, val+i+maxright[i])
        return ans
