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
#             if left == right:
#                 return
#             pivot_ind = random.randint(left, right)
#             pivot_ind = partition(left, right, pivot_ind, lst)
​
#             if pivot_ind < k_smallest: #go right
#                 quick_select(pivot_ind+1, right, k_smallest, lst)
#             elif pivot_ind > k_smallest: #go left
#                 quick_select(left, pivot_ind-1, k_smallest, lst)
#             return
​
#         n = len(nums)
#         quick_select(0, n-1, n-k, nums)
#         return nums[n-k]
