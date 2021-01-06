class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []
​
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.stack_min:
            self.stack_min.append(x)
        else:
            if self.stack[-1] <= self.stack_min[-1]:
                self.stack_min.append(x)
        
    def pop(self) -> None:  
        if self.stack_min[-1] == self.stack.pop():
            self.stack_min.pop()
​
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
​
    def getMin(self) -> int:
        return self.stack_min[-1] if self.stack_min else None
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
