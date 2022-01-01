class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #Greedy approach using heap, Time O(NlogN), Space O(N)
        if len(sticks) == 1: 
            return 0
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            cost += stick1 + stick2
            heapq.heappush(sticks, stick1+stick2)
        return cost
            
            
