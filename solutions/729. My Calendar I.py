class MyCalendar:
    #Bisect + insert by otoc, amortized time O(logN), space O(N)
    def __init__(self):
        self.starts = []
        self.ends = []
        
    def book(self, start, end):
        i = bisect.bisect_left(self.starts, start)
        if i - 1 >= 0 and start < self.ends[i-1]:
            return False
        if i < len(self.starts) and end > self.starts[i]:
            return False
        self.starts.insert(i, start)
        self.ends.insert(i, end)
        return True
    
#     #First attempt, use heap, amortized time O(NlogN), space O(N)
#     def __init__(self):
#         self.events = []
#         heapq.heapify(self.events)
​
#     def book(self, start: int, end: int) -> bool:
#         if not self.events:
#             heapq.heappush(self.events,(start,end))
#             return True
        
#         stack = []
#         while self.events and self.events[0][1] <= start:
#             stack.append(heapq.heappop(self.events))
        
#         if self.events and self.events[0][0] < end :
#             while stack:
#                 heapq.heappush(self.events,stack.pop())
#             return False
#         else:
#             heapq.heappush(self.events,(start,end))
#             while stack:
#                 heapq.heappush(self.events,stack.pop())
#             return True
​
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
