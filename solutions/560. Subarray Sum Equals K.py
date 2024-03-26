from collections import defaultdict
​
​
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = defaultdict(int)
        cur_sum, ans = 0, 0
        for num in nums:
            cur_sum += num
            #situation 1: prefix sum equal targetSum
            if cur_sum == k: ans += 1
            #situation 2: subarray starting in middle equal targetSum
            #proof: cur_sum - (cur_sum - target) = target
            ans += lookup[cur_sum-k]
            #update
            lookup[cur_sum] += 1
        return ans
