class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # soln 2 - O(N), dynamic programming
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
        
        #soln 1 - Kadane's algorithm
        #https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
        # cur_sum = max_sum = nums[0]
        # for i in range(1, len(nums)):
        #     cur_sum = max(nums[i], cur_sum + nums[i])
        #     max_sum = max(cur_sum, max_sum)
        # return max_sum
        
        # #soln 0 - brute force O(N^2), time exceeded
        # ans, n = nums[0], len(nums)
        # for i in range(1,n+1):
        #     for j in range(n-i+1):
        #         ans = max(ans, sum(nums[j:i+j]))
        # return ans
