class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #soln 0 - first attempt w Jake Reschke, stack, Time O(N), Space O(N)
        stack = []
        oper = {"+": lambda x,y: x + y, "-": lambda x,y: x - y, "*": lambda x,y: x * y, "/": lambda x,y: int(x/y)}
        
        for s in tokens:
            if s not in oper:
                stack.append(s)
            else:
                last = int(stack.pop())
                sec_last = int(stack.pop())
                stack.append(oper[s](sec_last, last))
            
        return stack[-1]
