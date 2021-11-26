class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int: 
        #Could not solve in first attempts, criterion: A[i+2]-A[i+1] == A[i+1]-A[i]
        #soln 3 - use math formula, time O(N), space O(1)
        count, ans = 0, 0
        for i in range(len(nums)-2):
            if nums[i+2]-nums[i+1] == nums[i+1]-nums[i]:
                count += 1
            else:
                ans += (count+1)*count//2
                count = 0
        return ans + (count+1)*count//2
        
        # #soln 1 - Leetcode DP optimized, very intuitive, time O(N), space O(1)
        # n = len(nums)
        # dp, ans = 0, 0
        # for i in range(n-2):
        #     if nums[i+2]-nums[i+1] == nums[i+1]-nums[i]:
        #         dp = 1 if i == 0 else dp+1
        #         ans += dp
        #     else:
        #         dp = 0
        # return ans
        
        # #soln 0 - Leetcode DP, very intuitive, time O(N), space O(N)
        # n = len(nums)
        # dp, ans = [0]*(n-2), 0
        # for i in range(n-2):
        #     if nums[i+2]-nums[i+1] == nums[i+1]-nums[i]:
        #         dp[i] = 1 if i == 0 else dp[i-1]+1
        #         ans += dp[i]
        # return ans
        
        # #soln 2 - Leetcode recursion, Time O(N), Space O(N)
        # self.ans = 0
        # def helper(nums, i):
        #     if i < 2: return 0
        #     ap = 0
        #     if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
        #         ap = 1 + helper(nums, i-1)
        #         self.ans += ap
        #     else:
        #         helper(nums, i-1)
        #     return ap
        # helper(nums, len(nums)-1)
        # return self.ans
