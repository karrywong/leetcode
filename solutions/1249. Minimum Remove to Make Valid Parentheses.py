class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #Leetcode two-pass string builder
        # Pass 1: Remove all invalid ")"
        first_pass_chars = []
        balance = 0
        open_seen = 0
        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            if c == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(c)
​
        # Pass 2: Remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance
        for c in first_pass_chars:
            if c == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(c)
​
        return "".join(result)
        
#         #First attempt, mock interview on 10/24
#         #Three passes, time O(N), space O(N)
#         # eg1, "lee(t(c)o)de)" -> "(()))" -> "(())"
#         stack = []
#         tbremoved = []
#         for i, char in enumerate(s): 
#             if char == "(":
#                 stack.append((char,i))
#             if char == ")":
#                 if not stack or stack[-1][0] != "(":
#                     tbremoved.append(i)
#                 else:
#                     stack.pop()
        
#         while stack: 
#             tbremoved.append(stack.pop()[1])
        
#         return ''.join([char for i, char in enumerate(s) if i not in tbremoved])        
