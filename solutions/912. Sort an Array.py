#         for i in range(1,n):
#             bisect.insort_left(nums, nums.pop(i), 0, i)
#         return nums
        
#         #5 counting sort, short implementation
#         counter = collections.Counter(nums)
#         return [i for i in range(min(counter), max(counter)+1) for _ in range(counter[i])]
        
#         #6. quicksort, Time O(NlogN)
#         def partition(l, r):
#             pivot_index = random.randint(l, r)
#             pivot = nums[pivot_index] # randomly choose an element as pivot, instead of the rightmost
#             nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            
#             i = l # pointer for greater element
#             for j in range(l, r):
#                 if nums[j] <= pivot:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     i += 1
#             nums[i], nums[r] = nums[r], nums[i]
#             return i      
        
#         def quicksort(lo, hi):
#             if lo < hi:
#                 p = partition(lo, hi)
#                 quicksort(lo, p - 1) # recursive call on the left of pivot
#                 quicksort(p + 1, hi) # recursive call on the right of pivot
        
#         quicksort(0, len(nums)-1)
#         return nums
        
#         #7. mergesort with recursion, Time O(NlogN), by dlwsdqdws
#         if len(nums) <= 1: return nums
#         middle = len(nums) // 2
#         left = self.sortArray(nums[:middle])
#         right = self.sortArray(nums[middle:])
#         merged = []
#         while left and right:
#             if left[0] <= right[0]:
#                 merged.append(left.pop(0))
#             else:
#                 merged.append(right.pop(0))
#         merged.extend(right if right else left)
#         return merged
        
#         #My soln 2 - heapsort using built-in heapq
#         heapq.heapify(nums)
#         return [heapq.heappop(nums) for i in range(len(nums))]       
