class Solution:
    def maxArea(self, height: List[int]) -> int:
        ### Soln 0 - two pointers, LeetCode solution beats me!!!
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
