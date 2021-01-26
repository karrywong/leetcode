class MyCalendar:
​
    def __init__(self):
        self.lst = []
​
    def book(self, start: int, end: int) -> bool:
        ### Soln 0 - slow, check self.lst every time
        if self.lst:
            for i in range(len(self.lst)):
                if self.lst[i][0] <= start < self.lst[i][1] or start <= self.lst[i][0] < end:
                    return False
        self.lst.append([start, end])
        return True
            
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
