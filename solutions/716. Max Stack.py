class MaxStack:
#     #soln 1 by gabbu in discussion, idea - Use a stack where each element is a tuple of (x, indexOfMaxSoFar).
#     #Time O(N), space O(N)
#     def __init__(self):
#         self.lst = []
 
#     def push(self, x: int) -> None:
#         if len(self.lst) == 0:
#             self.lst.append((x,0))
#         elif x >= self.lst[self.lst[-1][1]][0]:
#             self.lst.append((x,len(self.lst)))
#         else:
#             self.lst.append((x,self.lst[-1][1]))
        
#     def pop(self) -> int:
#         return self.lst.pop()[0]
    
#     def top(self) -> int:
#         return self.lst[-1][0]
​
#     def peekMax(self) -> int:
#         return self.lst[self.lst[-1][1]][0]
​
#     def popMax(self) -> int:
#         max_idx = self.lst[-1][1]
#         temp = []
#         t_idx = len(self.lst)-1
#         while t_idx != max_idx:
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
