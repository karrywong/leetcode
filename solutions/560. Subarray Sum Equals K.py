from collections import defaultdict
​
​
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         prefix sum + hash_table lib, time O(N), space O(N)
#         x = cur_sum - k <> k = cur_sum - x = (a+...+f) - (a+b) = c+e=f
#         [a, b, c, e, f, g]
        
        ans, cur_sum = 0, 0
        lib = defaultdict(int)
        for num in nums: 
            cur_sum += num # 3
            if cur_sum == k: ans += 1
        
            ans += lib[cur_sum-k] # 
            lib[cur_sum] += 1
        return ans
​
#         # failed attempt, time O(N)
#         # two ptr = sliding window, time O(N), space O(1)
#         ans, cur_sum = 0, 0
#         left = 0
#         for right, num in enumerate(nums):  # 2,1
#             cur_sum += num
#             if cur_sum == k: ans += 1
            
#             # while left < right and cur_sum >= k:
#             while left < right and abs(cur_sum-nums[left]-k) < abs(cur_sum-k):
#                 cur_sum -= nums[left]
#                 left += 1
#                 if cur_sum == k: ans += 1
            
#         return ans
    
    # testing
    # nums = [1,1,1], k = 2, cur_sum = 1
    #             |
    # left = 2
    # ans = 1+1
        
        
