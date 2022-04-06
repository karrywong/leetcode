class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #Eight sorting algorithm by junaidmansuri
        #1. selection sort, time O(N^2)
        #find minimum of list, removing it from original list, and appending it to answer
        # ans = []
        # for i in range(n-1,-1,-1):
        #     ind = min(range(i,-1,-1), key = lambda x: nums[x])
        #     ans.append(nums.pop(ind))
        # return ans
    
        #2. bubble sort, time O(N^2), repeatedly swapping adjacent elements that are out of order.
        # bo = True
        # while bo:
        #     bo = False
        #     for i in range(n-1):
        #         if nums[i] > nums[i+1]:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
        #             bo = True
        # return nums
        
        #3. insertion sort, time O(N^2), 
        #sequentially inserting element into proper location within sorted front portion of the original list. 
        # for i in range(1, n):
        #     for j in range(0,i):
        #         if nums[i] < nums[j]:
        #             nums.insert(j, nums.pop(i))
        #             break
        # return nums
    
        # #4. insertion sort with binary search improvement, time O(N^2)
        # for i in range(1,n):
        #     bisect.insort_left(nums, nums.pop(i), 0, i)
        # return nums
        
        #5. mergesort with recursion, Time O(NlogN), by dlwsdqdws
        if len(nums) <= 1: return nums
        middle = len(nums) // 2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])
        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(right if right else left)
        return merged
        
        # #My soln 2 - heapsort using built-in heapq
        # heapq.heapify(nums)
        # return [heapq.heappop(nums) for i in range(len(nums))]
