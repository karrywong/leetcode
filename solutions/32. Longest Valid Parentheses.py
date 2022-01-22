class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #Two pointers, inspired by LeetCode, time O(N), space O(1)
        ans = 0
        l, r = 0, 0 
        for i in range(len(s)): #left to right
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, 2*l)
            elif l < r:
                l, r = 0,0
                
        l, r = 0,0
        for i in range(len(s)-1, -1, -1): #right to left
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, 2*r)
            elif l > r:
                l, r = 0,0
        return ans
        
        # #LeetCode stack, time O(N), space O(N)
        # #Learn the trick of initializing stack as [-1] and length(i - stack[-1])
        # stack = [-1]
        # ans = 0
        # for i, char in enumerate(s):
        #     if char == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if stack:
        #             ans = max(ans, i - stack[-1])
        #         else:
        #             stack.append(i)
        # return ans
