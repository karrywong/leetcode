class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        #Mock interview, time O(N), space O(1)
        l, r = 0, len(plants)-1
        count = 0
        waterA, waterB = capacityA, capacityB
        
        while l < r:
            if waterA < plants[l]:
                count += 1
                waterA = capacityA
            waterA -= plants[l]
            l += 1
            
            if waterB < plants[r]:
                count += 1
                waterB = capacityB
            waterB -= plants[r]
            r -= 1
            
        return count+1 if l == r and waterA < plants[l] and waterB < plants[r] else count
    
        #eg1, l, r = 0,3, waterA,B = 3, 2 -> l,r=1,2, waterA,B = 1,2->5->2 -> l,r = 2,1
        #count = 1
