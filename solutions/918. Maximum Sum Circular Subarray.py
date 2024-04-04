class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         #Soln 3 - LeetCode montonic queue, time O(N), space O(N)
#         n = len(nums)
#         prefixSum = [0] + nums[:] + nums[:]
#         for i in range(1,len(prefixSum)):
#             prefixSum[i] += prefixSum[i-1]
            
#         # Want largest P[j] - P[i] with 1 <= j-i <= N
#         # For each j, want smallest P[i] with i >= j-N
#         ans = nums[0]
#         dq = collections.deque([0]) # i's, increasing by P[i]
#         for j in range(1, len(prefixSum)):
#             if dq[0] < j - n:
#                 dq.popleft()
#             # The optimal i is deque[0], for cand. answer P[j] - P[i]
#             ans = max(ans, prefixSum[j] - prefixSum[dq[0]])
#             # Remove any i1's with P[i2] <= P[i1].
#             while dq and prefixSum[j] <= prefixSum[dq[-1]]: #i so that P_i is smallest
#                 dq.pop()
#             dq.append(j)
#         return ans
​
        #Soln 2 - minimum subrray, modification from Kadane's algorithm
        #Time O(N), space O(1)
        cur_max = cur_min = 0
        max_sum = min_sum = nums[0]
        total_sum = 0
        
        for num in nums:
            cur_max = max(num, cur_max+num)
            max_sum = max(max_sum, cur_max)
            
            cur_min = min(num, cur_min+num)
            min_sum = min(min_sum, cur_min)
            
            total_sum += num
            
        if total_sum == min_sum:
            return max_sum
        return max(max_sum, total_sum-min_sum) 
​
        
#         # Soln 1 - prefix and suffix sums, modification from Kadane's algorithm
#         #Time O(N), space O(N)
#         n = len(nums)
#         right_max = [0]*n
#         right_max[-1] = nums[-1]
#         suffix_sum = nums[-1]
        
#         for i in range(n-2,-1,-1):
#             suffix_sum += nums[i]
#             right_max[i] = max(right_max[i+1], suffix_sum)
            
#         cur_sum = 0 
#         max_sum = nums[0]
#         special_sum = nums[0]
#         prefix_sum = 0
#         for i in range(n):
#             cur_sum = max(nums[i], cur_sum+nums[i])
#             max_sum = max(max_sum, cur_sum)
            
#             prefix_sum += nums[i]
#             if i+1<n:
#                 special_sum = max(special_sum, prefix_sum+right_max[i+1])
#         return max(max_sum, special_sum)
        
        # #TLE: Brute force from Kadane's algorithm, time O(N^2), space O(1)
        # ans = nums[0]
        # for k in range(len(nums)):
        #     cur_sum = nums[k]
        #     max_sum = nums[k]
        #     for i in range(k+1,k+len(nums)):
        #         if i >= len(nums):
        #             i %= len(nums)
        #         cur_sum = max(nums[i], cur_sum+nums[i])
        #         max_sum = max(max_sum, cur_sum)
        #     ans = max(ans, max_sum)
        # return ans
