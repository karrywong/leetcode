class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # eg1, "lee(t(c)o)de)" -> "(()))" -> "(())"
        stack = []
        tbremoved = []
        for i, char in enumerate(s): 
            if char == "(":
                stack.append((char,i))
            if char == ")":
                if not stack or stack[-1][0] != "(":
                    tbremoved.append(i)
                else:
                    stack.pop()
        
        while stack: 
            char, i = stack.pop()
            tbremoved.append(i)
        
        lst = [char for i, char in enumerate(s) if i not in tbremoved]
        return ''.join(lst)        
