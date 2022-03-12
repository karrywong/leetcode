from collections import deque
class MyStack:
​
    def __init__(self):
        self.q1 = deque()
​
    def push(self, x: int) -> None:
        # n = len(self.q1)
        # self.q1.append(x)
        # for _ in range(n):
        #     self.q1.append(self.q1.popleft())
        
        #faster
        self.q1 = deque([x]) + self.q1
​
    def pop(self) -> int:
        return self.q1.popleft()
​
    def top(self) -> int:
        return self.q1[0]
​
    def empty(self) -> bool:
        return not self.q1
​
​
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
