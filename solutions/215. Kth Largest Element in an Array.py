import heapq
# import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        min_num = min(nums)
        
        count = [0] * (max_num-min_num+1)
        for num in nums:
            count[num - min_num] += 1
        
        for idx in range(len(count)-1,-1, -1):
            k -= count[idx]
            if k <= 0:
                ans = idx
                break
                
        return ans + min_num
        
#         # min heap, time O(Nlogk), space O(k)
#         hp = []
#         heapq.heapify(hp)
​
#         for num in nums:
#             if len(hp) < k:
#                 heapq.heappush(hp, num)
#             elif hp[0] < num:
#                 heapq.heappushpop(hp, num)
# # OR 
