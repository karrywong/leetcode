class Solution:
    def decodeString(self, s: str) -> str:
        #Leetcode soln 2 w two stacks, one for count and one for string
        ctStack, strStack = [], [] #stacks
        curstr, k = "", 0
​
        for e in s:
            if e.isdigit(): 
                k = k * 10 + int(e)
            elif e == '[':
                ctStack.append(k) #push the number k to countStack
                strStack.append(curstr) #push the currentString to stringStack
                curstr, k = "", 0
            elif e == ']':
                decoded = strStack.pop()
                # decode currentK[currentString] by appending currentString k times
                decoded += curstr * ctStack.pop()
                curstr = decoded
            else:
                curstr += e
            #print(e, ctStack, strStack, curstr, k)
        return curstr
        
        
        #Modified Leetcode soln 1 w stack of single character or digit
        # stack = [] 
        # for i in range(len(s)):
        #     e = s[i]
        #     if e == "]":
        #         decoded = ""
        #         #get encoded string
        #         while stack[-1] != "[":
        #             decoded += stack.pop();
        #         stack.pop() #pop [ from stack
