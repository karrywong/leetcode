class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # #Naive attempt, LTE
        # m, n = len(nums1), len(nums2)
        # lst = itertools.product(nums1, nums2)
        # if m*n < k: 
        #     return lst
        # return heapq.nsmallest(k,lst,key = lambda x : x[0]+x[1])
        
        #Heap soln by vanquil in discussion
        s1 = min(k//2 + 2, len(nums1))
        s2 = min(k//2 + 2, len(nums2))
        
        heap = []
        for i in range(s1):
            for j in range(s2):
                heapq.heappush(heap, (nums1[i]+nums2[j], nums1[i], nums2[j]))
        ans = []
        while heap and len(ans) < k:
            x = heapq.heappop(heap)
            ans.append((x[1], x[2]))
        return ans
