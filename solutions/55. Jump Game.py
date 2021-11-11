class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # #soln 1 - LeetCode Greedy
        # n = len(nums)
        # lastPos = n - 1
        # for i in range(n-2,-1,-1):
        #     if i + nums[i] >= lastPos:
        #         lastPos = i
        # return lastPos == 0
        
        #soln 2 - Leetcode DP bottom-up w memoization
        n = len(nums)
        memo = ['U'] * n 
        memo[-1] = 'G'
        for i in range(n-2,-1,-1):
            furthestJump = min(i+nums[i], n-1)
            for j in range(i+1, furthestJump+1):
                if memo[j] == 'G':
                    memo[i] = 'G'
                    break
        return memo[0] == 'G'
        
        # #soln 0 - first attempt by Jake, Time O(n), Space O(1)
        # jump = False
        # j = 0
        # for i in range(len(nums)-2,-1,-1):
        #     if not jump and nums[i] > 0:
        #         continue
        #     elif not jump and nums[i] == 0:
        #         jump = True
        #         j = 0
        #     else:
        #         j += 1
        #         if nums[i] > j:
        #             jump = False
