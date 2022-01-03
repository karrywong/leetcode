class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #LeetCode, two pass, more efficient, time O(N), space O(1)
        left, right, count = {}, {}, collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
        
        ans = len(nums)
        max_freq = max(count.values())
        for x in count:
            if count[x] == max_freq:
                ans = min(ans, right[x]-left[x]+1)
        return ans
        
#         #First attempt, two pass, time O(N), space O(1)
#         count = collections.Counter(nums)
#         max_freq = max(count.values())
#         max_nums = {}
#         ind = 0
#         for k in count:
#             if count[k] == max_freq:
#                 max_nums[k] = ind
#                 ind += 1
#         if len(max_nums) == len(nums):
#             return 1
        
#         indices = [-1] * len(max_nums)
#         count = [0] * len(max_nums)
#         ans = float('inf')
#         for i, num in enumerate(nums):
#             if num in max_nums:
#                 if indices[max_nums[num]] == -1:
#                     indices[max_nums[num]] = i 
#                 count[max_nums[num]] += 1 
#                 if count[max_nums[num]] == max_freq:
#                     ans = min(ans, i - indices[max_nums[num]] + 1)
#         return ans
