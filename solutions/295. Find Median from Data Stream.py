class MedianFinder:
    def __init__(self):        
        self.maxHeap = [] #first half of all numbers
        self.minHeap = [] #second half of all numbers
​
    def addNum(self, num: int) -> None:
        #Add num to maxHeap
        #balancing two heaps
        if len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap, -1*num)
            return
        
        temp = -1*heapq.heappushpop(self.maxHeap, -1*num)
        heapq.heappush(self.minHeap, temp)
        
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap))
        
            
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0] 
        else:
            return 0.5*(-1*self.maxHeap[0]+self.minHeap[0])
​
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
