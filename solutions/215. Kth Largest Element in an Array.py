class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Sorting, time O(NlogN), space O(1)
        nums.sort()
        return nums[-k]
        
        #Heap, time O(NlogK), Space O(k)
        # return heapq.nlargest(k, nums)[-1]
