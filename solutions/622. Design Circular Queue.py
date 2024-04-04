​
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.count += 1
        return True
​
    def deQueue(self) -> bool:
        # if self.count == 0:
        #     return False
        # self.head_idx = (self.head_idx + 1) % self.capacity
        # self.count -= 1
        # return True
        
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True
​
    def Front(self) -> int:
        # if self.count == 0:
        #     return -1
        # return self.queue[self.head_idx % self.capacity]
        
        if self.count == 0:
            return -1
        return self.head.value
​
    def Rear(self) -> int:
        # if self.count == 0:
        #     return -1
        # return self.queue[(self.head_idx + self.count - 1) % self.capacity]
        
        if self.count == 0:
            return -1
        return self.tail.value
​
    def isEmpty(self) -> bool:
        return self.count == 0
    
    def isFull(self) -> bool:
        return self.count == self.capacity
​
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
