class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            width = right-left
            if height[left] >= height[right]:
                ans = max(ans, height[right]*width)
                right -= 1
            else:
                ans = max(ans, height[left]*width)
                left += 1
        return ans
