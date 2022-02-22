class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #LeetCode DP, much cleaner,  time O(target*len(nums)), space O(target)
        nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for comb_sum in range(target+1):
            for num in nums:
                if comb_sum < num:
                    break
                dp[comb_sum] += dp[comb_sum-num]
        return dp[target]        
        
        # #DP, time O(target*len(nums)),  space O(target), example 1
        # #[1, 1, 1, 1, 1]
        # #[1, 1, 2, 3, 5]
        # #[1, 1, 2, 4, 7]
        # nums.sort()
        # tb = [1] + [0] * target
        # for i in range(len(nums)):
        #     for val in range(nums[i], target+1):
        #         if i == 0 and val % nums[i] == 0:
        #             tb[val] += 1
        #         else:
        #             if val == nums[i]:
        #                 tb[val] += 1
        #             elif val > nums[i]:
        #                 tb[val] = 0
        #                 for num in nums:
        #                     if num >= val:
        #                         break
        #                     tb[val] += tb[val-num]
        # return tb[-1]
        
        # #First attempt, backtracking, time O(N^target) with N=len(nums), LTE
        # count = 0
        # def backtrack(num = target):
        #     nonlocal count
        #     if num == 0:
        #         count += 1
        #         return 
        #     if num < 0:
        #         return
        #     for i in range(len(nums)):
        #         backtrack(num-nums[i])
        # backtrack()
        # return count
