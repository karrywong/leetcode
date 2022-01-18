class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # #brute force better, time O(N^2), space O(1)
        # ans = 0
        # for i in range(len(heights)):
        #     min_height = heights[i]
        #     for k in range(i,-1,-1):
        #         min_height = min(min_height, heights[k])
        #         ans = max(ans, min_height * (i-k+1))
        # return ans
        
        #LeetCode stack, time O(N), space O(N), more challenging problem 85. Maximal Rectangle
        ans = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ans = max(ans, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        
        while stack[-1] != -1:
            ans = max(ans, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return ans
