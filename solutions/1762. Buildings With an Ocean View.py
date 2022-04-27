class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #First attempt - Time O(N), space O(1)
        n = len(heights)
        ans = [n-1]
        max_heights = heights[-1] #space optimization, O(N) -> O(1)
        
        for i in range(n-2,-1,-1):
            if heights[i] > max_heights:
                max_heights = heights[i] 
                ans.append(i)
                
        return ans[::-1]
