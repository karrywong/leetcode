class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #Eight sorting algorithm by junaidmansuri
        #1. selection sort, time O(N^2) - CLRS book done w/ swapping
        #find minimum of list, removing it from original list, and appending it to answer
        # ans = []
        # for i in range(n-1,-1,-1):
        #     ind = min(range(i,-1,-1), key = lambda x: nums[x])
        #     ans.append(nums.pop(ind))
        # return ans
    
        #2. bubble sort, time O(N^2), repeatedly swapping adjacent elements that are out of order.
        # bo = True
        # while bo:
        #     bo = False
        #     for i in range(n-1):
        #         if nums[i] > nums[i+1]:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
        #             bo = True
        # return nums
        
        #3. insertion sort, time O(N^2), 
        #sequentially inserting element into proper location within sorted front portion of the original list. 
        # for i in range(1, n):
        #     for j in range(0,i):
        #         if nums[i] < nums[j]:
        #             nums.insert(j, nums.pop(i))
        #             break
        # return nums
    
        # #4. insertion sort with binary search improvement, time O(N^2)
        # for i in range(1,n):
        #     bisect.insort_left(nums, nums.pop(i), 0, i)
        # return nums
        
        #5 counting sort, short implementation
        counter = collections.Counter(nums)
        return [i for i in range(min(counter), max(counter)+1) for _ in range(counter[i])]
        
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
