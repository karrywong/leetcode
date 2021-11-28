class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #First attempt, pairwise comparison, Time O(N^2), Space O(N)
        n = len(points)
        if n == 1: return 1
        ans = 2 #minimal answer is 2 if given two or more points
        for i in range(n-1):
            if ans >= n-i: break
            x, y = points[i]
            slopes = [None]*(n-i-1)
            for j in range(i+1,n):
                nom = points[j][1] - y
                denom = points[j][0] - x
                if denom == 0:
                    slopes[j-i-1] = float('inf')
                elif nom == 0:
                    slopes[j-i-1] = 0
                else:
                    slopes[j-i-1] = nom/denom
            count = collections.Counter(slopes)
            ans = max(ans, max(count.values())+1)
        return ans 
            
