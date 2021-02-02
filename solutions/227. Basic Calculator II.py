class Solution:
    import re
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        lst = list(reversed(re.split('([^0-9])',s)))
        stack = [i for i, x in enumerate(lst) if x == '*' or x == '/']
        
        res = 0
        while stack:
            idx = stack.pop()
            if lst[idx] == '*':
                lst[idx - 1 : idx + 2] = [str(int(lst[idx-1]) * int(lst[idx+1]))]
            else:
                lst[idx - 1 : idx + 2] = [str(int(lst[idx+1]) // int(lst[idx-1]))]
        
        res = int(lst[-1])
        i = len(lst) - 1
        while i > 0:
            if lst[i] == '+':
                res += int(lst[i-1])
                i -= 1
            if lst[i] == '-':
                res -= int(lst[i-1])
                i -= 1 
            i -= 1            
        return res            
                
