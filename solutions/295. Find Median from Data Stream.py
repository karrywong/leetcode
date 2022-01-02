class MedianFinder:
​
    def __init__(self):
        # self.lst = [] #trivial list sort, time O(NlogN)
        
        self.maxHeap = [] #first half of all numbers
        self.minHeap = [] #second half of all numbers
​
    def addNum(self, num: int) -> None:
        #self.lst.append(num)
        
        #Add num to maxHeap
        #balancing two heaps
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -1*num)
        else:
            heapq.heappush(self.maxHeap, -1*num)
            heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap))
        
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap))
    def findMedian(self) -> float:
        # self.lst.sort()
        # return self.lst[len(self.lst)//2] if len(self.lst) % 2 == 1 else 0.5*(self.lst[len(self.lst)//2-1] + self.lst[len(self.lst)//2])
        
        return -1*self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else 0.5*(-1*self.maxHeap[0]+self.minHeap[0])
​
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
