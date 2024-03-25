# import heapq
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    # # start time: 7:40pm
    # # min heap, time O(Nlogk), space O(k)
        hp = []
        heapq.heapify(hp)
        for num in nums: #num = 6
            if len(hp) >= k:
                heapq.heappushpop(hp, num) 
            else:
                heapq.heappush(hp, num)
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
    #Heap, time O(NlogK), Space O(k)
    # return heapq.nlargest(k, nums)[-1]
    
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
​
#             store_ind = l
#             for i in range(l,r):
#                 if lst[i] < pivot:
#                     lst[store_ind], lst[i] = lst[i], lst[store_ind]
#                     store_ind += 1
#             lst[store_ind], lst[r] = lst[r], lst[store_ind]
#             return store_ind
​
#         def quick_select(left:int, right:int, k_smallest:int, lst:List[int]) -> None:
