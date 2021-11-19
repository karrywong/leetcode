class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Recent attempt, keeping track of maximal and minimal values
        #Time O(N), Space O(1)
        ans, maxval, minval = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            temp1 = maxval*n
            temp2 = minval*n
            maxval = max(temp1, temp2, n)
            minval = min(temp1, temp2, n)
            ans = max(ans, maxval, minval)
        return ans
        
