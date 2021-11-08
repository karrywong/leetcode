class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        #soln 0 - first attempt, bit manipulation, Time O(n), Space O(1)
        ans = 0
        for n in nums:
            ans ^= n
        return ans
    
        # #math, Time O(n), Space O(n)
        # return 2*sum(set(nums)) - sum(nums)
