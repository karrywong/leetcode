class KthLargest:
​
    def __init__(self, k: int, nums: List[int]):
        #First attempt
        # self.minHeap = [num for num in nums[0:k]]
        # heapq.heapify(self.minHeap)
        # for num in nums[k:]:
        #     if num > self.minHeap[0]:
        #         heapq.heapreplace(self.minHeap, num)
        # self.k = k 
        
        #Leetcode, much cleaner
        self.k = k 
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        # if len(self.minHeap) < self.k:
        #     heapq.heappush(self.minHeap, val)
        #     return self.minHeap[0]
        # peekNum = self.minHeap[0]
        # if val < peekNum:
        #     return peekNum
        # else:
        #     heapq.heapreplace(self.minHeap, val)
        #     return self.minHeap[0]
        
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
