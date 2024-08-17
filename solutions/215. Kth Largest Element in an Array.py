import heapq
# import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap, time O(Nlogk), space O(k)
        hp = []
        heapq.heapify(hp)
​
        for num in nums:
            if len(hp) < k:
                heapq.heappush(hp, num)
            elif hp[0] < num:
                heapq.heappushpop(hp, num)
# OR 
            # if len(hp) >= k:
            #     heapq.heappushpop(hp, num) 
            # else:
            #     heapq.heappush(hp, num)  
        return hp[0]
​
    # # time O(N), space O(len(cnt) = (max_val - min_val) / step_size)
    # # cnt = [1, .., 3, 4, 1] #O(N)
    # cul_sum = 0
    # for i in range(len(cnt)-1,-1,-1):
    #     cul_sum += cnt[i]
    #     if cul_sum >= k:
    #         return i
    # return 
​
    # Heap, time O(NlogK), Space O(k)
        # return heapq.nlargest(k, nums)[-1]
        # return heapq.nsmallest(len(nums)-k+1,nums)[-1]
    
    # num = [499, 1, 5, 40,....]
    # nums = [3,2,3,1,2,4,5,5,6], k = 4
    # hp = [4,5,5,6]
    # <- decreasing order
    # return 4
    
#     # quick select, average time O(N), worst time O(N^2), space O(N)
#         def partition(l:int, r:int, p:int, lst:List[int]) -> int:
#             # all elements less than pivot are on the left. Otherwise, on the right
#             pivot = lst[p]
#             lst[p], lst[r] = lst[r], lst[p]
