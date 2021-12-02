class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #soln 2 - use python bisect(), refer <https://docs.python.org/3/library/bisect.html>
        #Time O(NlogN), space O(N)
        n, sub = len(nums), [nums[0]]
        for i in range(1,n):
            j = bisect_left(sub, nums[i]) #return index j such that #nums[i] <= sub[j] 
            if j == len(sub):
                sub.append(nums[i])
            else:
                sub[j] = nums[i]
        return len(sub)
    
        #soln 1 - Leetcode build subsequence, time O(N^2), space O(N)
        # n, sub = len(nums), [nums[0]]
        # for i in range(1,n):
        #     if sub[-1] >= nums[i]:
        #         j = 0
        #         while nums[i] > sub[j]:
        #             j += 1
        #         sub[j] = nums[i] #nums[i] <= sub[j] 
        #     else: #sub[-1] < nums[i]
        #         sub.append(nums[i])
        # return len(sub)
                
        # #soln 0 - Leetcode DP, time O(N^2), space O(N)
        # n = len(nums)
        # dp = [1] * n 
        # for i in range(1,n):
        #     for j in range(0,i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
