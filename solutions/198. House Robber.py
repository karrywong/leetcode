class Solution:
    def rob(self, nums: List[int]) -> int:
        # #soln 2 - Leetcode optimized DP, bottom-up w tabulation
        # #time O(N), space O(1)
        # n = len(nums)
        # if n <= 2: return max(nums)
        # RobNextNext = 0
        # RobNext = nums[n-1]
        # for i in range(n-2, -1, -1):
        #     current = max(RobNext, RobNextNext+nums[i])
        #     RobNextNext = RobNext
        #     RobNext = current
        # return current
        
        # #soln 1 - recursion with memoization
        # n = len(nums)
        # memo = {}
        # def helper(i):
        #     if i >= n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     val = max(helper(i+1), helper(i+2) + nums[i])
        #     memo[i] = val
        #     return val
        # return helper(0)
        
        #soln 3 - recursion w/ cache
        @lru_cache(maxsize = None)
        def helper(i):
            if i >= len(nums):
                return 0
            return max(helper(i+1), helper(i+2) + nums[i])
        return helper(0)
        
        # #soln 0 - dynamic programming
        # n = len(nums)
        # if n <= 2: return max(nums)
        # nums[2] += nums[0]
        # for i in range(3,n):
        #     nums[i] += max(nums[i-2], nums[i-3])
        # return max(nums[-2],nums[-1])
