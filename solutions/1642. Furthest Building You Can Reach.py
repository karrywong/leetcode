class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        #Inspired by LeetCode solution, clever use of heap
        climbs = [(heights[i+1]-heights[i], i) for i in range(len(heights)-1) if heights[i] < heights[i+1]]
        if not climbs: 
            return len(heights)
​
        count = 0
        ladder_alloc = []
        ans = climbs[count][1] if climbs else 0 
        while count < len(climbs):
            bo = False
            if ladders > 0: 
                heapq.heappush(ladder_alloc, climbs[count][0])
                ladders -= 1
            elif bricks >= 0:
                if ladder_alloc:
                    if ladder_alloc[0] > climbs[count][0]:
                        bricks -= climbs[count][0]
                    else:
                        val = heapq.heapreplace(ladder_alloc, climbs[count][0])
                        bricks -= val
                else:
                    bricks -= climbs[count][0]
                if bricks < 0:
                        return climbs[count][1]
            count += 1
        
        return len(heights)-1 if count == len(climbs) else ans
