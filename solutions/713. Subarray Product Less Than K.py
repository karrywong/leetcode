class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #first attempt, prefix product + sliding windows
        #time O(N), space O(1)
        ans = 0
        cur_prod, j = 1, 0
        for i, num in enumerate(nums):
            cur_prod *= num
            while j <= i and cur_prod >= k:
                cur_prod /= nums[j]
                j += 1
            ans += i-j+1
        return ans
        
#         # Lang like C++ that have overflow issue, use log
#         # binary search + prefix sum
#         if k == 0: return 0
#         log_k = math.log(k)
#         logs_prefix_sum = [0]
#         for num in nums:
#             logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num)) #prefix[i+1] = nums[0] + .. + nums[i]
            
#         ans = 0 
#         for i, log_sum in enumerate(logs_prefix_sum):
#             sum_val = log_k + log_sum - 1e-9 
#             l, r = i+1, len(logs_prefix_sum)
#             while l < r:
#                 mid = l + (r-l)//2
#                 if logs_prefix_sum[mid] < sum_val:
#                     l = mid+1
#                 else: 
#                     r = mid
#             # j = bisect.bisect(logs_prefix_sum, log_sum + log_k - 1e-9, i+1)
#             ans += l - i - 1
#         return ans
