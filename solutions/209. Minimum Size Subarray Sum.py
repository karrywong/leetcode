class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ### Soln 1 - brute force, O(n^2) time exceeded
#         if len(nums) == 0: return 0
        
#         ans = inf
#         sums = [None] * len(nums)
        
#         sums[0] = nums[0]
#         for i in range(1, len(nums)):
#             sums[i] = sums[i-1] + nums[i]
            
#         for i in range(0, len(nums)):
#             for j in range(i, len(nums)):
#                 val = sums[j] - sums[i] + nums[i] # sum of subarray i to j
#                 if val >= s:
#                     ans = min(ans, j - i + 1)
#                     break
#         return ans if ans != inf else 0
​
        ### Soln 2 - brute force with binary search, improved O(nlogn)
#         if len(nums) == 0: return 0 
        
#         ans = inf
#         sums = [0] * (len(nums) + 1)
        
#         for i in range(1, len(nums) + 1):
#             sums[i] = sums[i-1] + nums[i-1]
            
#         for i in range(1, len(nums) + 1):
#             to_find = s + sums[i-1]
#             greater_to_find = [v for v, x in enumerate(sums) if x >= to_find]
#             if greater_to_find:
#                 ans = min(ans, greater_to_find[0]-i+1)
​
#         return ans if ans != inf else 0
​
        ### Soln 3 - two pointer O(n)
        ans = inf
        left = 0 #pointer 1
        sums = 0
        for i in range(0, len(nums)):
            sums += nums[i]
