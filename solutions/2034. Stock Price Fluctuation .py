import heapq
class StockPrice:
    #{} key: timestamp, value: price
    #update: O(logN)
    #max, min: O(logN)
    #current: O(1)
    
    def __init__(self):
        self.htb = {} #key: timestamp, value: version
        self.maxhp = []
        self.minhp = []
        self.latest = [0, None] #[time, price]
        
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.htb:
            self.htb[timestamp] += 1
        else:
            self.htb[timestamp] = 1
        if timestamp >= self.latest[0]:
            self.latest[0] = timestamp
            self.latest[1] = price
            
        heappush(self.maxhp, (-price, timestamp, self.htb[timestamp]))
        heappush(self.minhp, (price, timestamp, self.htb[timestamp]))
        
    def current(self) -> int:
        return self.latest[1]
​
    def maximum(self) -> int:
        while self.htb[self.maxhp[0][1]] != self.maxhp[0][2] and self.maxhp:
            heappop(self.maxhp)
        return -self.maxhp[0][0] if self.maxhp else None
​
    def minimum(self) -> int:
        while self.htb[self.minhp[0][1]] != self.minhp[0][2] and self.minhp:
            heappop(self.minhp)
        return self.minhp[0][0] if self.minhp else None                 
​
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
