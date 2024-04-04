class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # DP in-place, time O(N), space O(1)
        # for i in range(1, len(nums)):
        #     if nums[i-1] > 0:
        #         nums[i] += nums[i-1]
        # return max(nums)
        
        #soln 1 - Kadane's algorithm, time O(N), space O(1)
        #https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
        cur_sum = 0
        max_sum = nums[0]
        for num in nums:
            cur_sum = max(num, cur_sum+num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
        
#         #soln 2 - O(NlogN), Leetcode divide and conquer
#         def findBestSubarray(nums, l, r):
#             if l > r:
#                 return float('-inf')
​
#             mid = (l + r )//2
            
#             #left half - iterate from the middle to the beginning
#             lcurr = best_lsum = 0
#             for i in range(mid-1, l-1, -1):
#                 lcurr += nums[i]
#                 best_lsum = max(best_lsum, lcurr)
            
#             #right half - iterate from the middle to the end
#             rcurr = best_rsum = 0
#             for i in range(mid+1, r+1):
#                 rcurr += nums[i]
#                 best_rsum = max(best_rsum, rcurr)
            
#             # Find the best subarray possible, left half, right half, and combined
#             combined = nums[mid] + best_lsum + best_rsum
#             left_half = findBestSubarray(nums, l, mid - 1)
#             right_half = findBestSubarray(nums, mid + 1, r)
            
#             # The largest of  is the answer for any given input array.
#             return max(combined, left_half, right_half)
        
#         return findBestSubarray(nums, 0, len(nums)-1)
