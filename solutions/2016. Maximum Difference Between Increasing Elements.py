class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #soln 0 - first attempt, Time O(N)
        #identical to 121. Best Time to Buy and Sell Stock
        minval = nums[0]
        ans = -1
        for n in nums:
            if n > minval:
                ans = max(ans,n - minval)
            else:
                minval = n
        return ans
