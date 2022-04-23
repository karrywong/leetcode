from functools import cmp_to_key
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        #soln by malraharsh, following the hints, time O(NlogN), space O(1)
        def sorter(x, y):
            n, m = len(x), len(y)
            if n != m:
                return -1 if n < m else 1 # when n > m
            else:
                return -1 if x < y else 1 if x > y else 0
            
        key = cmp_to_key(sorter)
        nums.sort(key=key, reverse=True)
        return nums[k-1]
        
        
#         #Quickselect, time O(N^2), space O(N)
#         nums[:] = sorted([int(num) for num in nums])
#         def partition(left:int, right:int, pivot_index:int) -> int:
#             pivot = nums[pivot_index]
#             nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
#             store_index = left
#             for i in range(left, right):
#                 if nums[i] < pivot:
#                     nums[store_index], nums[i] = nums[i], nums[store_index]
#                     store_index += 1
#             nums[store_index], nums[right] = nums[right], nums[store_index]
#             return store_index
        
#         def quick_select(left:int, right:int, k_smallest:int) -> None:
#             if left == right:
#                 return
#             pivot_index = random.randint(left, right)
#             pivot_index = partition(left, right, pivot_index)
            
#             if k_smallest == pivot_index:
#                 return
#             elif k_smallest < pivot_index: #go left
#                 quick_select(left, pivot_index - 1, k_smallest)
#             else: #go right
#                 quick_select(pivot_index + 1, right, k_smallest)            
            
#         n = len(nums)
#         quick_select(0, n - 1, n - k)
#         return str(nums[n-k])
        
        # #Heapsort, time O(NlogN), space O(N)
        # nums[:] = sorted([int(num) for num in nums])
        # return str(heapq.nlargest(k, nums)[-1])
        
        # #Built-in timsort
        # nums[:] = sorted([int(num) for num in nums])
        # nums.sort()
        # return str(nums[len(nums)-k])
