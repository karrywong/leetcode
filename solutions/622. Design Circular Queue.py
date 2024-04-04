class Node:
    def __init__(self, value:int, nextNode=None):
        self.value = value
        self.next = nextNode
        
class MyCircularQueue:
    def __init__(self, k: int):
        # # Array approach, (self.head_idx+self.count)%self.capacity
        # self.queue = [0]*k
        # self.head_idx = 0
        # self.count = 0
        # self.capacity = k
        
        # LinkList
        self.count = 0  
        self.capacity = k
        self.head = None
        self.tail = None
​
    def enQueue(self, value: int) -> bool:
        # if self.count == self.capacity:
        #     return False
        # idx = (self.head_idx + self.count) % self.capacity
        # self.queue[idx] = value
        # self.count += 1
        # return True
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
