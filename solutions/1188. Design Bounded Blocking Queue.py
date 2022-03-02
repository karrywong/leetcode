import threading
​
class BoundedBlockingQueue(object):
    #Learned threading.Condition from lamnguyen2187, refer to <https://docs.python.org/3/library/threading.html>
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cur = 0
        self.queue = collections.deque()
        self.cond = threading.Condition()
​
    def enqueue(self, element: int) -> None:
        self.cond.acquire()
        while self.cur >= self.cap:
            self.cond.wait()
        
        self.queue.append(element)
        self.cur += 1
​
        self.cond.notifyAll()
        self.cond.release()
​
    def dequeue(self) -> int:
        self.cond.acquire()
        while self.cur == 0:
            self.cond.wait()
            
        element = self.queue.popleft()
        self.cur -= 1
        
        self.cond.notifyAll()
        self.cond.release()
        
        return element
​
    def size(self) -> int:
        return self.cur
