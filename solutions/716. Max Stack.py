#             x,i = self.lst.pop()
#             temp.append(x)
#             t_idx -= 1
#         ans = self.lst.pop()[0]
#         while temp:
#             self.push(temp.pop())
#         return ans
​
    #soln 2 by xllllx in discussion, idea - use stack and maxHeap, passed by reference, smart!!!
    #Time O(logN), space O(N)
    def __init__(self):
        self.stack = []
        self.maxHeap = []
        heapq.heapify(self.maxHeap)
        self.TS = float('-inf')
​
    def push(self, x: int) -> None:
        entry = [-x, -len(self.stack)]
        heapq.heappush(self.maxHeap, entry)
        self.stack.append(entry)
        
    def pop(self) -> int:
        self.rm_tombstones()
        entry = self.stack.pop()
        entry[1] = self.TS
        return -entry[0]
    
    def top(self) -> int:
        self.rm_tombstones()
        return -self.stack[-1][0]
​
    def peekMax(self) -> int:
        self.rm_tombstones()
        return -self.maxHeap[0][0]
​
    def popMax(self) -> int:
        self.rm_tombstones()
        entry = heappop(self.maxHeap)
        entry[1] = self.TS
        return -entry[0]
    
    def rm_tombstones(self):
        while self.stack[-1][1] == self.TS:
            self.stack.pop()
        while self.maxHeap[0][1] == self.TS:
            heapq.heappop(self.maxHeap)        
​
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
