class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #LeetCode's quickselect, time O(N^2), space O(N)
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_freq = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            unique[right], unique[store_index] = unique[store_index], unique[right]
            return store_index
        
        def quick_select(left, right, k_smallest) -> None:
            if left == right:
                return
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index: #go left
                quick_select(left, pivot_index - 1, k_smallest)
            else: #go right
                quick_select(pivot_index + 1, right, k_smallest)
                
        n = len(unique)
        quick_select(0, n - 1, n - k)
        return unique[n-k:]
    
        # #Heapq built-in nlargest function, time O(NlogN), space O(N)
        # if k == len(nums):
        #     return nums
        # count = Counter(nums)   
        # return heapq.nlargest(k, count.keys(), key=count.get)        
