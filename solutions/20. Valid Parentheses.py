class Solution:
    def isValid(self, s: str) -> bool:
        # ### Soln 1 - stack
        # if len(s) % 2: return False
        # else:      
        #     stack = []
        #     mapping = {")": "(", "}": "{", "]": "["}
        #     for char in s: 
        #         if char in mapping: 
        #             top_element = stack.pop() if stack else '#'
        #             if mapping[char] != top_element:
        #                 return False
        #         else:
        #             stack.append(char)
        # return not stack
        
        #soln 1 - first attempt, be careful of stack being empty
        if len(s) % 2: return False
        stack = []
        lib = {'(': ')', '{':'}', '[':']'}
        for p in s:
            if p in lib:
                stack.append(p)
            else:
                if not stack:
                    return False
                if p != lib[stack.pop()]:
                    return False
        return stack == []
    
        ### Soln 0
        # temp = []
        # i = 0 
