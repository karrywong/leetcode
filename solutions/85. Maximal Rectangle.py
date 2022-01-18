class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         #soln 2 - Leetcode DP w max height at each point, originated from morrischen2008
#         if not matrix: return 0
#         m, n = len(matrix), len(matrix[0])
#         left = [0] * n # initialize left as the leftmost boundary possible
#         right = [n] * n # initialize right as the rightmost boundary possible
#         height = [0] * n
#         maxarea = 0
        
#         for i in range(m):
#             cur_left, cur_right = 0, n
#             for j in range(n): # update height
#                 if matrix[i][j] == '1': height[j] += 1
#                 else: height[j] = 0
                    
#             for j in range(n): # update left
#                 if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
#                 else:
#                     left[j] = 0
#                     cur_left = j + 1
                    
#             for j in range(n-1, -1, -1): # update right
#                 if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
#                 else:
#                     right[j] = n
#                     cur_right = j 
            
#             # print(height, left, right)
#             for j in range(n): # update the area
#                 maxarea = max(maxarea, height[j] * (right[j] - left[j]))
#         return maxarea
​
        #soln 1 - reuse histogram from 84. Largest Rectangle in Histogram
        #Time O(NM), space O(M)
        ans = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            ans = max(ans, self.largestRectangleArea(dp))
        return ans
    
    def largestRectangleArea(self, heights: List[int]):
        stack = [-1]
        recArea = 0
        for i in range(len(heights)):
            while stack != [-1] and heights[stack[-1]] > heights[i]:
                recArea = max(recArea, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
​
        while stack[-1] != -1:
            recArea = max(recArea, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return recArea
​
#         #soln 0 - better brute force, time O(N^2*M), space O(NM)
#         #Alternative using row time O(N*M^2)
#         ans = 0
#         dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == "0": continue
#                 dp[i][j] = dp[i][j-1]+1 if j>0 else 1
#                 width = dp[i][j]
                
#                 for k in range(i, -1, -1):
#                     width = min(width, dp[k][j])
#                     ans = max(ans, (i-k+1)*width)
#         return ans
