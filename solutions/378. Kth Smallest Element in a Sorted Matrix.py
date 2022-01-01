class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #Completely failed, no solution
        #Leetcode Heap approach - treat matrix as N sorted list
        m = len(matrix)
        #Initialization
        heap = []
        for r in range(min(k, m)):
            heap.append((matrix[r][0], r, 0))
            heapq.heapify(heap)
        while k:
            val, r, c = heapq.heappop(heap)
            if c < m-1:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
            k -= 1
        return val
                
        
        
            
                
        
