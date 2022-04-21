class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        #Straightforward, one-sweep, time O(N), space O(1)
        minval = float('inf')
        maxval = float('-inf')
        
        for num in nums:
            minval = min(minval, num)
            maxval = max(maxval, num)
        
        return max(0, maxval-minval-2*k)
