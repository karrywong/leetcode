class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
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
        
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    to_removed.append(i)
        
        to_removed.extend(stack) # sorted
        # return "".join([s[i] for i in range(len(s)) if i not in to_removed])
        
        ptr = 0
        res = []
        for i,char in enumerate(s):
            if ptr < len(to_removed) and i == to_removed[ptr]:
                ptr += 1
                continue
            res.append(char)
        return "".join(res)
