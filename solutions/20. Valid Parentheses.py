class Solution:
    def isValid(self, s: str) -> bool:
        ### Soln 1
        # temp = []
        # i = 0 
        # if len(s) % 2: return False
        # else:
        #     while i < len(s):
        #         if s[i] in ["(", "{", "["]:
        #             temp.append(s[i])
        #         elif s[i] in [")", "}", "]"] and temp == []:
        #             return False
        #         else:
        #             if s[i] == ")" and temp[-1] != "(": return False
        #             if s[i] == "}" and temp[-1] != "{": return False
        #             if s[i] == "]" and temp[-1] != "[": return False
        #             temp.pop(-1)
        #         i += 1
        #     return False if temp else True
        
        
        ### Soln 2 - stack
        if len(s) % 2: return False
        else:      
            stack = []
            mapping = {")": "(", "}": "{", "]": "["}
            for char in s: 
                if char in mapping: 
                    top_element = stack.pop() if stack else '#'
                    if mapping[char] != top_element:
                        return False
                else:
                    stack.append(char)
        return not stack
​
