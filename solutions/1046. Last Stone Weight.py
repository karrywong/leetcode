class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Heap, time O(NlogN), space O(N)
        maxHeap = [-1* stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = -1*heapq.heappop(maxHeap)
            stone2 = -1*heapq.heappop(maxHeap)
            if stone1 < stone2: 
                heapq.heappush(maxHeap, stone1-stone2)
            elif stone1 > stone2:
                heapq.heappush(maxHeap, stone2-stone1)
        return -1*maxHeap[0] if maxHeap else 0
