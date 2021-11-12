class Solution:
    def maxArea(self, height: List[int]) -> int:
         ### Soln 0 - first attempt two pointers
        ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r-l
            if height[l] < height[r]:
                ans = max(ans, height[l] * width)
                l += 1
            else: 
                ans = max(ans, height[r] * width)
                r -= 1
        return ans
                
        
