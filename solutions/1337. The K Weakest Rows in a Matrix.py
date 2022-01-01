class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #LeetCode Heap + BS, time O(Mlog(NK)), 
        m, n = len(mat), len(mat[0])
        def bs(row): #binary search
            lo, hi = 0, n
            while lo < hi:
                mid = lo + ((hi-lo) >> 1)
                if row[mid] == 1:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        heap = [] #heapq.heapify(heap), not necessary
        for ind, row in enumerate(mat):
            i = bs(row)
            tp = (-i, -ind)
            if len(heap) < k or tp > heap[0]:
                heapq.heappush(heap, tp)
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while heap:
            _, ind = heapq.heappop(heap)
            ans.append(-ind)
        return ans[::-1]
        
        # #Heap, time O(MN+KlogM), space O(M)
        # heap = []
        # heapq.heapify(heap)
        # htb = collections.defaultdict(list)
        # for ind, row in enumerate(mat):
        #     i, j = 0, 0
        #     for val in row:
        #         if val:
        #             i += 1
        #         else:
        #             j += 1
        #     heapq.heappush(heap, (i,j))
        #     htb[(i,j)].append(ind)
        # ans = []
        # while len(ans) < k:
        #     tp = heapq.heappop(heap)
        #     if tp in htb:
        #         lst = htb[tp]
        #         for l in lst:
        #             ans.append(l)
        #             if len(ans) == k: break
        #         del htb[tp]
        # return ans
