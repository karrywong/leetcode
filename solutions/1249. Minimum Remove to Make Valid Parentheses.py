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
        
                    
