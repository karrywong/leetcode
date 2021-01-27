class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ### Soln 0 - Heap. time complexity O(Nlogk)
        #return heapq.nlargest(k, nums)[-1]
        
        ### Soln 1 - Quicksort, time complexity O(N) - LeetCode solution
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to the end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            #3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index
        
        def select(left, right, k_smallest):
            if left == right: #corner case: list contains only one element
                return nums[left]
            
            #select a random pivot_index in between
            pivot_index = random.randint(left, right)
            
            #find the pivot position in a sorted list:
            pivot_index = partition(left, right, pivot_index)
            
            #the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index-1, k_smallest)
            else:
