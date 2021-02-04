class Solution:
    def calculate(self, s: str) -> int:   
        ### Soln 0 - first attempt
        stack = []
        curnum = 0
        lib = {'+':1, '-':-1}
        sign = 1
        
        for i in s:
            if i == ' ':
                continue
            elif i.isalnum():
                curnum = curnum * 10 + int(i)
            elif i in '+-':
                stack.append(sign*curnum)
                curnum = 0
                sign = lib[i]
            elif i == '(':
                if sign == 1:
                    stack.append(i)
                else:
                    stack.append('-'+i)
                    sign = 1
            else:
                temp = sign*curnum
                curnum = 0
                while stack[-1] != '(' and stack[-1] != '-(':
                    temp += stack.pop()
                if stack.pop() == '(':
                    stack.append(temp)
                else:
