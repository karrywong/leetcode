class Solution:
    def trap(self, height: List[int]) -> int:
        #soln 2 - two pointers, Time O(N), Space O(1)
        n, ans = len(height), 0
        left, right = 0, n-1
        left_max, right_max = 0, 0
        while (left < right):
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1
        return ans 
    
        # #soln 1 - Leetcode stack
        # n, ans, curr = len(height), 0, 0
        # stack = []
        # while curr < n:
        #     while stack and height[curr] > height[stack[-1]]:
        #         top = stack[-1]
        #         stack.pop()
        #         if not stack:
        #             break
        #         width = curr - stack[-1] - 1
        #         bound = min(height[curr], height[stack[-1]]) - height[top]
        #         print(curr, ans, width * bound)
        #         ans += width * bound
        #     stack.append(curr)
        #     curr += 1
        # return ans
        
#         #soln 0 - extra space to record right/left maxima, Time O(N), Space O(N)
#         n, ans = len(height), 0
#         if n <= 2: return ans
#         rightmax = height.copy()
#         leftmax = height.copy()
#         for i in range(n-2,-1,-1):
#             rightmax[i] = max(rightmax[i], rightmax[i+1])
#         for i in range(1,n):
#             leftmax[i] = max(leftmax[i-1], leftmax[i])
#         for i in range(1,n-1):
#             ans += min(leftmax[i], rightmax[i]) - height[i]
#         return ans
