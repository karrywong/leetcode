class MyQueue:
    def __init__(self):
        # self.queue = collections.deque()
        self.s1 = [] #stack 1
        self.s2 = [] #stack 2
        
    def push(self, x: int) -> None:
        # self.queue.append(x)
        #Push O(N), pop O(1)
        # while self.s1:
        #     self.s2.append(self.s1.pop())
        # self.s1.append(x)
        # while self.s2:
        #     self.s1.append(self.s2.pop())
        
        #Push O(1), pop amortized O(1)
        self.s1.append(x)
​
    def pop(self) -> int:
        # return self.queue.popleft()
        #Push O(N), pop O(1)
        # return self.s1.pop()
        
        #Push O(1), pop amortized O(1)
        self.peek()
        return self.s2.pop()
​
    def peek(self) -> int:
        # return self.queue[0]
        #Push O(N), pop O(1)
        # return self.s1[-1]
        
        #Push O(1), pop amortized O(1)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        
    def empty(self) -> bool:
        # return not self.queue
        #Push O(N), pop O(1)
        # return not self.s1
                
        #Push O(1), pop amortized O(1)
        return not self.s1 and not self.s2
​
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
