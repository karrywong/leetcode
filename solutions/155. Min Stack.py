class MinStack:
    #soln 1 - two stacks optimized
    def __init__(self):
        self.stack = []
        self.minstack = []    
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1][0] > val:
                self.minstack.append([val,1])
            elif self.minstack[-1][0] == val:
                self.minstack[-1][1] += 1
        else:
            self.minstack.append([val,1])
        
    def pop(self) -> None: 
        if self.stack[-1] == self.minstack[-1][0]:
            if self.minstack[-1][1] == 1:
                self.minstack.pop()
            else:
                self.minstack[-1][1] -= 1
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minstack[-1][0]
    
#     #soln 0 - Leetcode min pair
#     def __init__(self):
#         self.stack = []
        
#     def push(self, val: int) -> None:
#         if self.stack:
#             self.stack.append([val, min(val, self.stack[-1][1])])
#         else:
#             self.stack.append([val,val])
            
#     def pop(self) -> None:
#         return self.stack.pop()[0]
​
#     def top(self) -> int:
#         return self.stack[-1][0]
​
#     def getMin(self) -> int:
#         return self.stack[-1][1]
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
