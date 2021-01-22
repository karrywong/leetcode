class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### Soln 1 - using heap structure
        counts = collections.Counter(nums)
        heap = [(v, k) for k, v in counts.items()]
        lst = heapq.nlargest(k, heap)
        res = [k for v, k in lst]
        return res
        
#         ### Soln 0 - O(nlogn), time complexity
#         counts = collections.Counter(nums) #hashtable
        
#         lst = [v for v in counts.values()]
#         lst.sort(reverse = True) #worst case O(nlog(n))
#         freq = lst[0:k] # largest k frequencies
        
#         res = [] 
#         # find the keys corresponding to the k frequencies
#         for i in range(k):
#             for k, v in counts.items():
#                 if v == freq[i] and k not in res:
#                     res.append(k)
#         return res
