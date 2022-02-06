class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #Soln 2 - LeetCode montonic queue
        n = len(nums)
        prefixSum = [0] + nums[:] + nums[:]
        for i in range(1,len(prefixSum)):
            prefixSum[i] += prefixSum[i-1]
            
        # Want largest P[j] - P[i] with 1 <= j-i <= N
        # For each j, want smallest P[i] with i >= j-N
        ans = nums[0]
        dq = collections.deque([0]) # i's, increasing by P[i]
        for j in range(1, len(prefixSum)):
            if dq[0] < j - n:
                dq.popleft()
            # The optimal i is deque[0], for cand. answer P[j] - P[i]
            ans = max(ans, prefixSum[j] - prefixSum[dq[0]])
            # Remove any i1's with P[i2] <= P[i1].
            while dq and prefixSum[j] <= prefixSum[dq[-1]]: #i so that P_i is smallest
                dq.pop()
            dq.append(j)
        return ans
        
#         #Soln 1 - Next Array, modification from Kadane's algorithm
#         #Time O(N), space O(N)
#         n = len(nums)
#         ans = cur_sum = nums[0]
#         for i in range(1,n):
#             cur_sum = max(nums[i], cur_sum + nums[i])
#             ans = max(ans, cur_sum)
#         print(ans)
#         #all 2-interval subarrays. For each i, we want to know
#         # the maximum of sum(A[j:]) with j >= i+2
#         rightsums = [0]*(n-1) + [nums[-1]]
#         maxright = [0]*(n-1) + [nums[-1]]
#         for i in range(n-2,-1,-1): 
#             rightsums[i] += rightsums[i+1] + nums[i] # rightsums[i] = sum(A[i:])
#             maxright[i] = max(maxright[i+1], rightsums[i])  #maxright[i] = max_{j >= i} rightsums[j]
        
#         leftsum = 0
#         for i in range(n-2):
#             leftsum += nums[i]
#             ans = max(ans, leftsum + maxright[i+2])
#         return ans
        
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
