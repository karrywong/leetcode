class Solution:
    def rob(self, nums: List[int]) -> int:
        #soln 1 - recursion with memoization
        n = len(nums)
        memo = {}
        def helper(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            val = max(helper(i+1), helper(i+2) + nums[i])
            memo[i] = val
            return val
        return helper(0)
        
        # #soln 0 - dynamic programming
        # n = len(nums)
        # if n <= 2: return max(nums)
        # nums[2] += nums[0]
        # for i in range(3,n):
        #     nums[i] += max(nums[i-2], nums[i-3])
        # return max(nums[-2],nums[-1])
        
