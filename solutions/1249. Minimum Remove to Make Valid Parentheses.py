class Solution:
    # "(()))" -> "", "()", "(())" 
    
    # time O(N), N = len(s), space O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack: list[tuple] (idx)
        stack = [] # parenthesis to remove
        for idx, char in enumerate(s): 
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(idx)
        if not stack:
            return s
        
        ans_list = []
        ptr = 0
        for idx, char in enumerate(s):
            if ptr < len(stack) and idx == stack[ptr]:
                ptr += 1
                continue
            ans_list.append(char)
        return "".join(ans_list)
    
# Testing 
# s = "e(t(c)o)d)"
#      |
# stack = [(),9)], ptr = 0
# ans_list[e,(, t, ..., d]
​
#         #Two-pass string builder
#         # Pass 1: compute balance; remove extra rightmost ")"
#         first_pass_chars = []
#         balance = 0
#         for char in s:
#             if char == "(":
#                 balance += 1
#             elif char == ")":
#                 if balance == 0:
#                     continue
#                 balance -= 1
#             first_pass_chars.append(char)
#         # balance >= 0     
        
#         second_pass_chars = []
#         for i in range(len(first_pass_chars)-1, -1, -1):
#             c = first_pass_chars[i]
#             if balance > 0 and c == "(":
#                 balance -= 1
#                 continue
#             second_pass_chars.append(c)
                
#         return "".join(second_pass_chars[::-1])
        
        # mock practice on 4/20
        # time O(N), space O(N), N = len(s)
        # pass with stack on (,), unbalance note index into removed index
        # while stack ->into removed index
        
        to_removed = []
        stack = [] # record ( index
        
