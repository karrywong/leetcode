class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # #first attempt, prefix product + sliding windows
        # #time O(N), space O(1)
        n, ans = len(nums), 0
        j, cur_prod = 0, 1
        for i in range(n):
            cur_prod *= nums[i]                
            while j <= i and cur_prod >= k:
                cur_prod /= nums[j]
                j += 1
            ans += i-j+1
        return ans
        
#         #Leetcode Soln using binary search, idea: take log, consider prefix sum, prefix[i+1] = nums[0] + .. + nums[i]
#         #for each i, the largest j so that nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k
#         #time O(NlogN), space O(1)
#         if k == 0: return 0
#         k = math.log(k)
#         prefixSum = [0] * (len(nums)+1)
#         for i in range(1, len(nums)+1):
#             prefixSum[i] += prefixSum[i-1] + math.log(nums[i-1]) #prefix[i+1] = nums[0] + .. + nums[i]
​
#         ans = 0 
#         for i, p in enumerate(prefixSum):
#             j = bisect.bisect(prefixSum, p+k-1e-9,i+1)
#             ans += j-i-1
#             # print(i,p, j, j-i-1)
#         return ans
