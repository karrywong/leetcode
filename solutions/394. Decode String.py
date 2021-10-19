class Solution:
    def decodeString(self, s: str) -> str:
        #Modified Leetcode soln 1 w stack of single character or digit
        stack = [] 
        for i in range(len(s)):
            if s[i] == "]":
                decoded = ""
                #get encoded string
                while stack[-1] != "[":
                    decoded += stack.pop();
                stack.pop() #pop [ from stack
                base, k = 1, 0
                while stack and stack[-1].isdigit():
                    k += int(stack.pop()) * base #get number k
                    base *= 10 
                #decode k[decodedString], by pushing decodedString k times into stack
                if k: stack.append(k*decoded)
                #print(i, stack, decoded)
            else:
                stack.append(s[i])
        return ''.join([i[::-1] for i in stack])
